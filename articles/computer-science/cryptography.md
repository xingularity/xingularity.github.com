# Cryptography

## RSA Algorithm

1. Choose two large primes $p$ and $q$
2. Compute $n = pq$ and $\phi(n) = (p-1)(q-1)$
3. Choose $e$ such that $\gcd(e, \phi(n)) = 1$
4. Compute $d \equiv e^{-1} \pmod{\phi(n)}$

**Encryption**: $c \equiv m^e \pmod{n}$
**Decryption**: $m \equiv c^d \pmod{n}$

## Hash Functions

Desired properties:
- **Pre-image resistance**: Given $h$, hard to find $m$ such that $H(m) = h$
- **Second pre-image resistance**: Given $m_1$, hard to find $m_2 \neq m_1$ such that $H(m_1) = H(m_2)$
- **Collision resistance**: Hard to find $m_1 \neq m_2$ such that $H(m_1) = H(m_2)$