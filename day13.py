class Solution:
    def graycode(self, n):
        result = []
        
        for i in range(1 << n):   # 2^n
            gray = i ^ (i >> 1)
            binary = format(gray, f'0{n}b')  # pad with leading zeros
            result.append(binary)
        
        return result
