class Solution:
    def articulationPoints(self, V, edges):
        from collections import defaultdict
        
        # Step 1: Build graph
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        # Step 2: Initialize
        disc = [-1] * V
        low = [-1] * V
        visited = [False] * V
        parent = [-1] * V
        ap = [False] * V  # articulation point marker
        
        time = [0]  # mutable time
        
        # Step 3: DFS function
        def dfs(u):
            visited[u] = True
            disc[u] = low[u] = time[0]
            time[0] += 1
            
            children = 0
            
            for v in adj[u]:
                if not visited[v]:
                    parent[v] = u
                    children += 1
                    dfs(v)
                    
                    # Update low value
                    low[u] = min(low[u], low[v])
                    
                    # Case 1: root node
                    if parent[u] == -1 and children > 1:
                        ap[u] = True
                    
                    # Case 2: non-root
                    if parent[u] != -1 and low[v] >= disc[u]:
                        ap[u] = True
                
                elif v != parent[u]:
                    low[u] = min(low[u], disc[v])
        
        # Step 4: Handle disconnected graph
        for i in range(V):
            if not visited[i]:
                dfs(i)
        
        # Step 5: Collect result
        result = [i for i in range(V) if ap[i]]
        
        return result if result else [-1]
