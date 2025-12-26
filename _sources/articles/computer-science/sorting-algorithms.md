# Sorting Algorithms

## Merge Sort

Divide and conquer algorithm with recurrence:

$$
T(n) = 2T(n/2) + \Theta(n)
$$

By the Master Theorem: $T(n) = \Theta(n \log n)$

## Quick Sort

Average case recurrence:

$$
T(n) = T(k) + T(n-1-k) + \Theta(n)
$$

Average time complexity: $\Theta(n \log n)$
Worst case: $\Theta(n^2)$