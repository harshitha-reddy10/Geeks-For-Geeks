class Solution:
    def countPartitions(self, arr, diff):
        total_sum = sum(arr)
        
        # If not possible
        if (total_sum + diff) % 2 != 0:
            return 0
        
        target = (total_sum + diff) // 2
        
        # DP array
        dp = [0] * (target + 1)
        dp[0] = 1  # one way to get sum 0
        
        for num in arr:
            for j in range(target, num - 1, -1):
                dp[j] += dp[j - num]
        
        return dp[target]
