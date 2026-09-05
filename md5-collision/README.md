# Cryptographic Hash Collisions & MD5 Suffix Preservation

## Objective
Generate MD5 cryptographic collisions using `md5collgen` and prove the **Collision Suffix-Preservation Property** inherent to Merkle-Damgård hash constructions.

## Environment & Tools
* **Tools:** `md5collgen`, `OpenSSL`, `GCC`
* **OS Environment:** SEED Ubuntu Linux

## Mechanics & Mathematical Concept
MD5 processes messages in sequential 512-bit blocks using an internal compression function $f$:
$$H_i = f(H_{i-1}, M_i)$$

When `md5collgen` creates two 128-byte block prefixes $P_1$ and $P_2$ where $f(H_{init}, P_1) = f(H_{init}, P_2)$, appending an identical binary suffix $T$ preserves digest equality:
$$MD5(P_1 \parallel T) = MD5(P_2 \parallel T)$$

## Execution Steps
1. Generated distinct 128-byte collision blocks $P_1$ and $P_2$ via `md5collgen`.
2. Verified initial block outputs yielded matching MD5 checksums.
3. Appended an identical trailing binary payload $T$ to both blocks and verified that outputs maintained matching checksums.
4. Embedded collision array blocks inside C programs to produce two executable binaries sharing an identical MD5 digest that execute separate code paths.

## Observations & Lessons
* Hash collision attacks disrupt systems relying on digests for software integrity or digital signatures.
* Merkle-Damgård constructions pass internal states forward, meaning identical intermediate compression states remain identical regardless of trailing data.

**Security Takeaway:** MD5 lacks collision resistance and should be replaced by SHA-256 or SHA-3 in secure systems.
