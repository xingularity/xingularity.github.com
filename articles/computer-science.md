# Computer Science and Algorithms

This article covers fundamental computer science concepts with mathematical formulations.

## Algorithm Analysis

### Big O Notation

We describe the asymptotic behavior of algorithms using Big O notation:

- **Constant time**: $O(1)$
- **Logarithmic time**: $O(\log n)$
- **Linear time**: $O(n)$
- **Linearithmic time**: $O(n \log n)$
- **Quadratic time**: $O(n^2)$
- **Exponential time**: $O(2^n)$

### Master Theorem

For recurrence relations of the form $T(n) = aT(n/b) + f(n)$:

$$
T(n) = \begin{cases}
\Theta(n^{\log_b a}) & \text{if } f(n) = O(n^{\log_b a - \epsilon}) \text{ for some } \epsilon > 0 \\
\Theta(n^{\log_b a} \log n) & \text{if } f(n) = \Theta(n^{\log_b a}) \\
\Theta(f(n)) & \text{if } f(n) = \Omega(n^{\log_b a + \epsilon}) \text{ for some } \epsilon > 0
\end{cases}
$$

## Data Structures

### Binary Search Trees

For a balanced binary search tree with $n$ nodes, the height is:

$$
h = \Theta(\log n)
$$

Search, insertion, and deletion operations take $O(\log n)$ time.

### Hash Tables

Expected time complexity for operations in a hash table with good hash function:

- **Search**: $O(1)$ average, $O(n)$ worst case
- **Insert**: $O(1)$ average, $O(n)$ worst case
- **Delete**: $O(1)$ average, $O(n)$ worst case

Load factor: $\alpha = \frac{n}{m}$ where $n$ is number of elements and $m$ is table size.

## Sorting Algorithms

### Merge Sort

Divide and conquer algorithm with recurrence:

$$
T(n) = 2T(n/2) + \Theta(n)
$$

By the Master Theorem: $T(n) = \Theta(n \log n)$

### Quick Sort

Average case recurrence:

$$
T(n) = T(k) + T(n-1-k) + \Theta(n)
$$

Average time complexity: $\Theta(n \log n)$
Worst case: $\Theta(n^2)$

## Graph Theory

### Graph Representations

For a graph $G = (V, E)$ with $|V| = n$ vertices and $|E| = m$ edges:

**Adjacency Matrix**: Space complexity $\Theta(n^2)$
**Adjacency List**: Space complexity $\Theta(n + m)$

### Shortest Path Algorithms

**Dijkstra's Algorithm**: Time complexity $O((V + E) \log V)$ with binary heap

**Bellman-Ford Algorithm**: Time complexity $O(VE)$

**Floyd-Warshall Algorithm**: Time complexity $\Theta(V^3)$

### Minimum Spanning Tree

**Kruskal's Algorithm**: $O(E \log E)$
**Prim's Algorithm**: $O(E \log V)$ with binary heap

## Information Theory

### Entropy

Shannon entropy of a random variable $X$:

$$
H(X) = -\sum_{i} p_i \log_2 p_i
$$

### Data Compression

**Huffman Coding**: Optimal prefix-free code with expected length:

$$
L = \sum_{i} p_i \ell_i \leq H(X) + 1
$$

where $\ell_i$ is the length of codeword for symbol $i$.

## Machine Learning

### Linear Regression

Cost function for linear regression:

$$
J(\theta) = \frac{1}{2m} \sum_{i=1}^{m} (h_\theta(x^{(i)}) - y^{(i)})^2
$$

Normal equation for optimal parameters:

$$
\theta = (X^T X)^{-1} X^T y
$$

### Gradient Descent

Parameter update rule:

$$
\theta_j := \theta_j - \alpha \frac{\partial}{\partial \theta_j} J(\theta)
$$

where $\alpha$ is the learning rate.

### Neural Networks

**Sigmoid activation function**:
$$
\sigma(z) = \frac{1}{1 + e^{-z}}
$$

**ReLU activation function**:
$$
\text{ReLU}(z) = \max(0, z)
$$

**Softmax function** for multi-class classification:
$$
\text{softmax}(z_i) = \frac{e^{z_i}}{\sum_{j=1}^{K} e^{z_j}}
$$

## Cryptography

### RSA Algorithm

1. Choose two large primes $p$ and $q$
2. Compute $n = pq$ and $\phi(n) = (p-1)(q-1)$
3. Choose $e$ such that $\gcd(e, \phi(n)) = 1$
4. Compute $d \equiv e^{-1} \pmod{\phi(n)}$

**Encryption**: $c \equiv m^e \pmod{n}$
**Decryption**: $m \equiv c^d \pmod{n}$

### Hash Functions

Desired properties:
- **Pre-image resistance**: Given $h$, hard to find $m$ such that $H(m) = h$
- **Second pre-image resistance**: Given $m_1$, hard to find $m_2 \neq m_1$ such that $H(m_1) = H(m_2)$
- **Collision resistance**: Hard to find $m_1 \neq m_2$ such that $H(m_1) = H(m_2)$

## Computational Complexity

### P vs NP

**P**: Problems solvable in polynomial time
**NP**: Problems verifiable in polynomial time

Open question: $P \stackrel{?}{=} NP$

### NP-Complete Problems

Examples:
- 3-SAT (Boolean satisfiability)
- Traveling Salesman Problem (decision version)
- Graph Coloring
- Subset Sum

If any NP-complete problem has a polynomial-time solution, then $P = NP$.