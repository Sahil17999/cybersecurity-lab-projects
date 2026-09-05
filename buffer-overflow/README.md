# Buffer Overflow Exploitation & Privilege Escalation

## Objective
Analyze a stack-based buffer overflow vulnerability in a Set-UID C executable and develop an exploit payload to overwrite saved frame pointers, redirect execution flow to an x86 shellcode payload, and run an elevated root shell (`euid = 0`).

## Environment Configuration
* **OS Environment:** SEED Ubuntu Linux
* **Compiler Flags:** `gcc -z execstack -fno-stack-protector` (Stack execution enabled, stack canaries disabled)
* **Kernel Configuration:** ASLR disabled via `sysctl` (`/proc/sys/kernel/randomize_va_space = 0`)

## Execution & Exploitation Steps
1. **Locating Stack Offsets:** Used GDB to inspect register states at the function prologue and measure the distance between the target buffer address and Saved Frame Pointer (`$ebp`):
   $$\text{Offset to } \$ebp = \text{Address}(\$ebp) - \text{Address}(\text{Buffer}) = 108 \text{ bytes}$$
   $$\text{Offset to Target Return Address } (\$eip) = 108 + 4 = 112 \text{ bytes}$$

2. **Payload Architecture:** Built a Python script (`exploit.py`) to output a byte stream combining a NOP sled (`0x90`), 27-byte x86 shellcode spawning `/bin/sh`, and the targeted return address pointing back into the NOP sled.

3. **Execution Result:** Redirected payload stream into the vulnerable executable, successfully triggering execution diversion and yielding an interactive root shell.

## Code Snippet (Exploit Logic)
