class Solution:
    def sortBySetBitCount(self, arr):
        # sort based on count of set bits (descending)
        arr.sort(key=lambda x: bin(x).count('1'), reverse=True)
        return arr
