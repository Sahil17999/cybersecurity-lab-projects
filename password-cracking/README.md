# Linux Password Hashing & Dictionary Attacks

## Objective
Extract salted password hashes from Linux shadow files (`/etc/shadow`) and execute offline dictionary attacks, local MD5 digest matching, and web-based credential brute-forcing using custom C and Python scripts (`level3.py`, `level4.py`, `level5.py`, `level6.py`, and `test.cs`)[cite: 3, 4, 5, 6, 7].

---

## Mechanics & Shadow Format
Linux systems store user authentication settings in `/etc/shadow`:
`username:$id$salt$hashed_value:lastchanged:min:max:warn:inact:expire`

Common algorithm identifiers ($id$) include:
* `$1$`: MD5-crypt
* `$5$`: SHA-256-crypt
* `$6$`: SHA-512-crypt[cite: 6]
* `$7$` / `$scrypt$`: scrypt KDF

Salts defeat **Pre-computed Rainbow Table Attacks** by ensuring identical passwords yield distinct outputs across different users ($H(\text{Password} \parallel \text{Salt})$).

---

## Execution & Attack Strategies

### 1. Offline Shadow Hash Cracking (`level6.py`)
Extracted the algorithm ID (`$6$`) and salt string (`$6$jJ70WFelxvD_wRqJ$`) from a target `/etc/shadow` entry[cite: 6]. Iterated through a candidate wordlist (`months.txt`) using Python's `crypt` module to generate candidate hashes until finding a match[cite: 6].

### 2. MD5 Digest Matching (`level5.py`)
Read plaintext wordlist entries from `months.txt`, derived their MD5 hex digests via `hashlib`, and checked them against a target digest string (`a0b629570a31f7e3e377d8eba828e414`)[cite: 5].

### 3. Online Web Application Brute-Force (`level4.py`)
Automated HTTP `GET` requests using `requests` with session cookies to submit candidate passwords from `months.txt` against a web endpoint (`http://localhost:8000/level/4`) until receiving an HTTP 200 success code[cite: 4].

### 4. Sequential PIN Enumeration (`level3.py`)
Executed an online numeric brute-force attack against an authenticated endpoint (`http://localhost:8000/level/3`) by generating zero-padded 3-digit PINs (`000`–`999`) using session cookies[cite: 3].

### 5. C Hash Generation Testing (`test.cs`)
Implemented a test script using `crypt.h` to pass a known password (`"password"`) and salt string (`"$y$j9T$t4HYYraTPjT8AtgercDbi."`) to `crypt()` and inspect the resulting hash output[cite: 7].

---

## Code Snippets

### Shadow File Parsing & Cracking (`level6.py`)
```python
import crypt

shadow = "alice:$6$jJ70WFelxvD_wRqJ$da5a71a994d6305665706242af8cbea84fc963d126f11ba44129c35d640161401b9b1174e09a6f1840227821477f5445a33e4af43ade0b3a6adaecb388f7308c:19447:0:99999:7:::"

target_hash = shadow.split(":")[1]
salt = "$6$" + target_hash.split("$")[2] + "$"

with open("months.txt", "r", encoding="utf-8", errors="ignore") as f:
	for line in f:
		password = line.strip()
		shadow_can = crypt.crypt(password, salt)

		if shadow_can == target_hash:
			print("Password Found:", password)
			break
