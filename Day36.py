class Solution:
    def longestSubstr(self, s, k):
        freq = [0] * 26
        left = 0
        max_freq = 0
        result = 0
        
        for right in range(len(s)):
            # Update frequency
            idx = ord(s[right]) - ord('A')
            freq[idx] += 1
            
            # Track max frequency in current window
            max_freq = max(max_freq, freq[idx])
            
            # If more than k changes needed, shrink window
            while (right - left + 1) - max_freq > k:
                freq[ord(s[left]) - ord('A')] -= 1
                left += 1
            
            # Update result
            result = max(result, right - left + 1)
        
        return result
