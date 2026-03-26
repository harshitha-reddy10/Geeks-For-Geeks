import heapq

class Solution:
    def countPaths(self, V, edges):
        MOD = 10**9 + 7
        
        graph = [[] for _ in range(V)]
        for u, v, t in edges:
            graph[u].append((v, t))
            graph[v].append((u, t))
        
        dist = [float('inf')] * V
        ways = [0] * V
        
        dist[0] = 0
        ways[0] = 1
        
        pq = [(0, 0)]
        
        while pq:
            d, node = heapq.heappop(pq)
            
            if d > dist[node]:
                continue
            
            for nei, wt in graph[node]:
                new_dist = d + wt
                
                if new_dist < dist[nei]:
                    dist[nei] = new_dist
                    ways[nei] = ways[node]
                    heapq.heappush(pq, (new_dist, nei))
                
                elif new_dist == dist[nei]:
                    ways[nei] += ways[node]
        
        return ways[V - 1] % MOD
