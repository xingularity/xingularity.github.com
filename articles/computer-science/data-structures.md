# Data Structures

## Binary Search Trees

For a balanced binary search tree with $n$ nodes, the height is:

$$
h = \Theta(\log n)
$$

Search, insertion, and deletion operations take $O(\log n)$ time.

## Hash Tables

Expected time complexity for operations in a hash table with good hash function:

- **Search**: $O(1)$ average, $O(n)$ worst case
- **Insert**: $O(1)$ average, $O(n)$ worst case
- **Delete**: $O(1)$ average, $O(n)$ worst case

Load factor: $\alpha = \frac{n}{m}$ where $n$ is number of elements and $m$ is table size.