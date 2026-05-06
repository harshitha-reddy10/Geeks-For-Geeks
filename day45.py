class Solution:
    def getSize(self, root):
        # Base case
        if root is None:
            return 0
        
        # Recursive case
        return 1 + self.getSize(root.left) + self.getSize(root.right)
        
