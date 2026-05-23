class Solution:
    def toSumTree(self, root):
        
        def solve(node):
            if not node:
                return 0
            
            old_val = node.data
            
            left_sum = solve(node.left)
            right_sum = solve(node.right)
            
            # Update current node with sum of left and right subtrees
            node.data = left_sum + right_sum
            
            # Return total sum of subtree including original node value
            return node.data + old_val
        
        solve(root)
