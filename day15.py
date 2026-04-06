import heapq

class Node:
    def __init__(self, freq, char=None):
        self.freq = freq
        self.char = char
        self.left = None
        self.right = None


class Solution:
    def huffmanCodes(self, s, f):
        heap = []
        order = 0
        
        # Step 1: push all characters
        for i in range(len(s)):
            heapq.heappush(heap, (f[i], order, Node(f[i], s[i])))
            order += 1
        
        # 🔴 Edge case: only one character
        if len(heap) == 1:
            return ["0"]
        
        # Step 2: build tree
        while len(heap) > 1:
            freq1, o1, left = heapq.heappop(heap)
            freq2, o2, right = heapq.heappop(heap)
            
            newNode = Node(freq1 + freq2)
            newNode.left = left
            newNode.right = right
            
            heapq.heappush(heap, (freq1 + freq2, min(o1, o2), newNode))
        
        root = heap[0][2]
        
        # Step 3: preorder traversal
        result = []
        
        def dfs(node, code):
            if not node:
                return
            
            if node.char is not None:
                result.append(code)
                return
            
            dfs(node.left, code + "0")
            dfs(node.right, code + "1")
        
        dfs(root, "")
        
        return result
