# Information Theory

## Entropy

Shannon entropy of a random variable $X$:

$$
H(X) = -\sum_{i} p_i \log_2 p_i
$$

## Data Compression

**Huffman Coding**: Optimal prefix-free code with expected length:

$$
L = \sum_{i} p_i \ell_i \leq H(X) + 1
$$

where $\ell_i$ is the length of codeword for symbol $i$.