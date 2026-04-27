class Solution:
    def smallestSubstring(self, s):
        count = {'0': 0, '1': 0, '2': 0}
        left = 0
        min_len = float('inf')
        
        for right in range(len(s)):
            count[s[right]] += 1
            
            # Check if all characters are present
            while count['0'] > 0 and count['1'] > 0 and count['2'] > 0:
                min_len = min(min_len, right - left + 1)
                
                # Shrink window
                count[s[left]] -= 1
                left += 1
        
        return min_len if min_len != float('inf') else -1
