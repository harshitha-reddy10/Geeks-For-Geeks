import math

class Solution:
    def minSteps(self, m, n, d):
        # If d is greater than both jugs
        if d > max(m, n):
            return -1
        
        # Check feasibility using GCD
        if d % math.gcd(m, n) != 0:
            return -1
        
        # Helper function to simulate pouring
        def pour(fromJug, toJug, d):
            fromCap = fromJug
            toCap = toJug
            
            fromJug = fromCap
            toJug = 0
            
            step = 1  # filling fromJug
            
            while fromJug != d and toJug != d:
                # Transfer water
                temp = min(fromJug, toCap - toJug)
                toJug += temp
                fromJug -= temp
                step += 1
                
                # Check if we got d
                if fromJug == d or toJug == d:
                    break
                
                # If fromJug becomes empty, fill it
                if fromJug == 0:
                    fromJug = fromCap
                    step += 1
                
                # If toJug becomes full, empty it
                if toJug == toCap:
                    toJug = 0
                    step += 1
            
            return step
        
        # Try both directions and take minimum
        return min(pour(m, n, d), pour(n, m, d))
