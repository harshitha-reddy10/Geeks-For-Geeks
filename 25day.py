class Solution:
    def myAtoi(self, s):
        i = 0
        n = len(s)
        
        # 1. Skip leading whitespaces
        while i < n and s[i] == ' ':
            i += 1
        
        # If string is empty after removing spaces
        if i == n:
            return 0
        
        # 2. Check sign
        sign = 1
        if s[i] == '+':
            i += 1
        elif s[i] == '-':
            sign = -1
            i += 1
        
        # 3. Read digits
        num = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])
            
            # 4. Handle overflow before adding digit
            if num > (2**31 - 1 - digit) // 10:
                return 2**31 - 1 if sign == 1 else -2**31
            
            num = num * 10 + digit
            i += 1
        
        return sign * num
