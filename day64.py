class Solution:
    def checkElements(self, start, end, arr):
        # Convert array into set for fast lookup
        s = set(arr)
        
        # Check every number in range [start, end]
        for i in range(start, end + 1):
            if i not in s:
                return False
        
        return True
