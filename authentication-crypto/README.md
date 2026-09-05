# Linux Password Hashing & Offline Dictionary Attack

## Objective
Extract salted password hashes from Linux shadow files (`/etc/shadow`) and execute an offline dictionary attack using a custom C program leveraging `libcrypt`.

## Mechanics & Shadow Format
Linux accounts store salted password hashes in `/etc/shadow`:
$$\texttt{username:\$id\$salt\$hashed\_value:lastchanged:min:max:warn:inact:expire}$$
* `\$1\$`: MD5-crypt
* `\$5\$`: SHA-256-crypt
* `\$6\$`: SHA-512-crypt
* `\$7\$` / `\$scrypt\$`: scrypt KDF

Salts prevent **Pre-computed Rainbow Table Attacks** by forcing per-user hash calculations ($H(\text{Password} \parallel \text{Salt})$).

## Execution Steps
1. Parsed target user entries from `/etc/shadow` to extract the algorithm ID and salt string.
2. Constructed a C program using `crypt_r()` to iterate through wordlist entries, applying the salt parameters to candidate passwords.
3. Compared computed hash strings against the shadow file target until identifying matching plaintext.
