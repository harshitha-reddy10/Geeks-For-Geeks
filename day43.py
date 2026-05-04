class Solution:
    def isBinaryPalindrome(self, n):
        binary = bin(n)[2:]   # convert to binary (remove '0b')
        return binary == binary[::-1]


# Main program
if __name__ == "__main__":
    n = int(input("Enter a number: "))
    
    sol = Solution()
    result = sol.isBinaryPalindrome(n)
    
    if result:
        print("True")
    else:
        print("False")
