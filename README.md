# cybersecurity-lab-projects

Welcome! This repository contains write-ups, custom exploit scripts, and cryptographic proofs developed during university computer security labs (ECE 458). Exercises use the SEED Labs environment on an isolated Ubuntu Linux system to explore memory safety vulnerabilities, low-level execution control, cryptographic weaknesses, and authentication mechanisms.

---

## 📄 Master PDF Reference

For the unified, single-document PDF version containing all module summaries and execution screenshots (ideal for offline viewing or LinkedIn Feature attachments), see:
* 📄 **[Cybersecurity Lab Portfolio (PDF)](./Cybersecurity_Lab_Portfolio.pdf)**

---

## 📁 Repository Modules

### 1. [Buffer Overflow Exploitation & Privilege Escalation](./buffer-overflow/)
* **Objective:** Exploit memory corruption in a Set-UID binary to hijack execution flow and acquire root access (`euid = 0`).
* **Key Skills:** GDB debugging, stack offset calculation, x86 assembly, shellcode injection, ASLR/NX/Canary evaluation.

### 2. [Cryptographic Hash Collisions & MD5 Analysis](./md5-collision/)
* **Objective:** Demonstrate MD5 collision generation and verify the collision suffix-preservation property.
* **Key Skills:** hash collision attacks, binary payload modification, Merkle-Damgård state analysis.

### 3. [Linux Password Hashing & Offline Dictionary Attacks](./password-cracking/)
* **Objective:** Extract salted shadow hashes from `/etc/shadow` and execute an offline dictionary attack using C and `libcrypt`.
* **Key Skills:** Key derivation functions (`scrypt`/SHA-512), salt mechanics, shadow password parsing.

### 4. [Symmetric Encryption & Token Authentication Models](./authentication-crypto/)
* **Objective:** Analyze block cipher pattern leakage in AES-ECB vs. CBC modes and evaluate entropy in token-based authentication systems.
* **Key Skills:** Block cipher evaluation, Initialization Vectors (IV), token entropy modeling, key lifecycle management.

---

## 🧰 Tools & Environment
* **Environment:** SEED Ubuntu Linux VM / Docker
* **Tools Used:** `GDB + PEDA`, `GCC`, `Python 3`, `libcrypt`, `md5collgen`, `OpenSSL`
* **Core Concepts:** x86 Assembly, Memory Safety, Privilege Boundaries, Cryptography, Identity Controls

## 🔗 Framework & Tooling References
* **SEED Security Labs:**
  * [Buffer Overflow Set-UID Lab Specification](https://seedsecuritylabs.org/Labs_20.04/Software/Buffer_Overflow_Setuid/)
  * [Crypto MD5 Collision Lab Specification](https://seedsecuritylabs.org/Labs_20.04/Crypto/Crypto_MD5_Collision/)
* **Analysis & Encoding Tools(Used in authenticaiton-crypto section):**
  * [CyberChef Analysis Suite (GCHQ)](https://gchq.github.io/CyberChef/)

> **Academic Integrity Notice:** All exercises were completed in isolated virtual environments using public SEED Labs frameworks for educational purposes.
