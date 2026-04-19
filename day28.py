class Solution:
    def isPower(self, x, y):
        # Special case
        if x == 1:
            return y == 1
        
        # Keep dividing y by x
        while y % x == 0:
            y = y // x
        
        # If y becomes 1, it's a power
        return y == 1
