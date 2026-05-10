class Solution:
    def maxProfit(self, x, y, a, b):
        n = len(a)
        
        # Store difference along with profits
        tasks = []
        for i in range(n):
            tasks.append((abs(a[i] - b[i]), a[i], b[i]))
        
        # Sort by maximum difference descending
        tasks.sort(reverse=True)
        
        profit = 0
        
        for diff, pa, pb in tasks:
            
            # If A gives more profit
            if pa >= pb:
                if x > 0:
                    profit += pa
                    x -= 1
                else:
                    profit += pb
                    y -= 1
            
            # If B gives more profit
            else:
                if y > 0:
                    profit += pb
                    y -= 1
                else:
                    profit += pa
                    x -= 1
        
        return profit
