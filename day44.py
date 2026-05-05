class Solution:
    def sumXOR(self, arr):
        n = len(arr)
        total_sum = 0
        
        # Check each bit position (0 to 31)
        for bit in range(32):
            count1 = 0
            
            # Count numbers with this bit set
            for num in arr:
                if num & (1 << bit):
                    count1 += 1
            
            count0 = n - count1
            
            # Contribution of this bit
            total_sum += count1 * count0 * (1 << bit)
        
        return total_sum
