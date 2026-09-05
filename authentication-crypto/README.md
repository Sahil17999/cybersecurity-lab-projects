# Symmetric Encryption Modes & Authentication Models

## Objective
Analyze structural pattern exposure in block cipher operational modes (AES-ECB vs. AES-CBC) and evaluate threat models and key management lifecycles in authentication systems.

## Key Concepts & Analysis

### 1. Block Cipher Operational Modes
* **Electronic Codebook (AES-ECB):** Encrypts plaintext blocks independently ($C_i = E_K(P_i)$). Deterministic block mapping leaks structural patterns present in plaintext inputs (e.g., bitmap images, structured file headers).
* **Cipher Block Chaining (AES-CBC):** XORs plaintext blocks with preceding ciphertext blocks ($C_i = E_K(P_i \oplus C_{i-1})$) using a randomized Initialization Vector ($C_0 = \text{IV}$). Randomized IVs hide structural patterns across identical plaintexts.

### 2. Key Lifecycle & Storage Boundaries
* **Data-at-Rest (DAR):** Long-term keys stored in key vaults, protected via access control lists and periodic key rotation schedules.
* **Data-in-Transit (DIT):** Ephemeral session keys established via Diffie-Hellman exchanges to enforce Perfect Forward Secrecy (PFS).

### 3. Authentication & Threat Modeling
* **Token Possession vs. Knowledge Factors:** Physical drawing-based tokens or physical cards combine possession controls with visual patterns.
* **Threat Surface:** Token systems must account for visual capture, physical duplication, and template compromise on backend authentication servers.

**Security Takeaway:** Deterministic ciphers like ECB leak plaintext patterns; secure encryption requires randomized IV modes alongside distinct key lifecycles for stored and transmitted data.
