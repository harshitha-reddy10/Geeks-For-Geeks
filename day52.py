class Solution:
    def findMotherVertex(self, V, edges):
        adj = [[] for _ in range(V)]
        
        for u, v in edges:
            adj[u].append(v)

        visited = [False] * V

        # DFS function
        def dfs(node):
            visited[node] = True
            for nei in adj[node]:
                if not visited[nei]:
                    dfs(nei)

        # Step 1: Find candidate mother vertex
        candidate = -1
        for i in range(V):
            if not visited[i]:
                dfs(i)
                candidate = i

        # Step 2: Verify candidate
        visited = [False] * V
        dfs(candidate)

        for v in visited:
            if not v:
                return -1

        # Step 3: Find smallest mother vertex
        # Check all vertices smaller than candidate
        for i in range(candidate):
            visited = [False] * V
            dfs(i)

            if all(visited):
                return i

        return candidate
