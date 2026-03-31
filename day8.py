class Solution:
    def maxProfit(self, arr, k):
        if not arr:
            return 0
        
        hold = -arr[0]   # profit when holding a stock
        cash = 0         # profit when not holding
        
        for i in range(1, len(arr)):
            prev_cash = cash
            
            # sell today or do nothing
            cash = max(cash, hold + arr[i] - k)
            
            # buy today or do nothing
            hold = max(hold, prev_cash - arr[i])
        
        return cash
