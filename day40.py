class Solution:
    def findPosition(self, n):
        # If n is 0 or has more than one set bit
        if n == 0 or (n & (n - 1)) != 0:
            return -1
        
        # Find position of the only set bit
        pos = 1
        while n > 1:
            n = n >> 1
            pos += 1
        
        return pos
