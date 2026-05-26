class Solution:
    def minToggle(self, arr):
        n = len(arr)
        
        # Prefix count of 1s
        prefix_ones = [0] * (n + 1)
        
        for i in range(n):
            prefix_ones[i + 1] = prefix_ones[i] + arr[i]
        
        ans = float('inf')
        
        # Try every partition point
        for i in range(n + 1):
            # Left side should be all 0s -> toggle 1s to 0s
            left_toggles = prefix_ones[i]
            
            # Right side should be all 1s -> toggle 0s to 1s
            right_toggles = (n - i) - (prefix_ones[n] - prefix_ones[i])
            
            ans = min(ans, left_toggles + right_toggles)
        
        return ans
