from collections import defaultdict, deque

class Solution:
    def minHeightRoot(self, V, edges):
        if V == 1:
            return [0]

        graph = defaultdict(list)
        degree = [0] * V

        # Build graph
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degree[u] += 1
            degree[v] += 1

        # Initial leaves
        leaves = deque()
        for i in range(V):
            if degree[i] == 1:
                leaves.append(i)

        remaining_nodes = V

        # Trim leaves
        while remaining_nodes > 2:
            size = len(leaves)
            remaining_nodes -= size

            for _ in range(size):
                leaf = leaves.popleft()

                for neighbor in graph[leaf]:
                    degree[neighbor] -= 1
                    if degree[neighbor] == 1:
                        leaves.append(neighbor)

        return list(leaves)
