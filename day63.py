class Solution:
    def coin(self, arr):
        left = 0
        right = len(arr) - 1
        
        # Continue until one coin remains
        while left < right:
            # Remove the larger coin from ends
            if arr[left] >= arr[right]:
                left += 1
            else:
                right -= 1
        
        return arr[left]
