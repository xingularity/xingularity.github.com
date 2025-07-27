# Algorithm Analysis

## Big O Notation

We describe the asymptotic behavior of algorithms using Big O notation:

- **Constant time**: $O(1)$
- **Logarithmic time**: $O(\log n)$
- **Linear time**: $O(n)$
- **Linearithmic time**: $O(n \log n)$
- **Quadratic time**: $O(n^2)$
- **Exponential time**: $O(2^n)$

## Master Theorem

For recurrence relations of the form $T(n) = aT(n/b) + f(n)$:

$$
T(n) = \begin{cases}
\Theta(n^{\log_b a}) & \text{if } f(n) = O(n^{\log_b a - \epsilon}) \text{ for some } \epsilon > 0 \\
\Theta(n^{\log_b a} \log n) & \text{if } f(n) = \Theta(n^{\log_b a}) \\
\Theta(f(n)) & \text{if } f(n) = \Omega(n^{\log_b a + \epsilon}) \text{ for some } \epsilon > 0
\end{cases}
$$