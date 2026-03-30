import heapq

class Solution:
    def minCost(self, houses):
        n = len(houses)
        visited = [False] * n
        min_heap = [(0, 0)]  # (cost, house_index)
        total_cost = 0
        
        while min_heap:
            cost, i = heapq.heappop(min_heap)
            
            if visited[i]:
                continue
            
            visited[i] = True
            total_cost += cost
            
            for j in range(n):
                if not visited[j]:
                    dist = abs(houses[i][0] - houses[j][0]) + abs(houses[i][1] - houses[j][1])
                    heapq.heappush(min_heap, (dist, j))
        
        return total_cost
