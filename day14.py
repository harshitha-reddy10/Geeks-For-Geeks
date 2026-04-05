class Solution:
    def totalWays(self, arr, target):
        S = sum(arr)
        
        # Edge cases
        if abs(target) > S or (S + target) % 2 != 0:
            return 0
        
        req = (S + target) // 2
        
        # DP array
        dp = [0] * (req + 1)
        dp[0] = 1   # one way to make sum 0
        
        for num in arr:
            for j in range(req, num - 1, -1):
                dp[j] += dp[j - num]
        
        return dp[req]
