# Graph Theory

## Graph Representations

For a graph $G = (V, E)$ with $|V| = n$ vertices and $|E| = m$ edges:

**Adjacency Matrix**: Space complexity $\Theta(n^2)$
**Adjacency List**: Space complexity $\Theta(n + m)$

## Shortest Path Algorithms

**Dijkstra's Algorithm**: Time complexity $O((V + E) \log V)$ with binary heap

**Bellman-Ford Algorithm**: Time complexity $O(VE)$

**Floyd-Warshall Algorithm**: Time complexity $\Theta(V^3)$

## Minimum Spanning Tree

**Kruskal's Algorithm**: $O(E \log E)$
**Prim's Algorithm**: $O(E \log V)$ with binary heap