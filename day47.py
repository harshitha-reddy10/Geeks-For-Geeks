from collections import deque

class Solution:
    def isValid(self, s):
        count = 0
        
        for ch in s:
            if ch == '(':
                count += 1
            elif ch == ')':
                count -= 1
                
                if count < 0:
                    return False
        
        return count == 0

    def validParenthesis(self, s):
        res = []
        visited = set()
        q = deque()

        q.append(s)
        visited.add(s)

        found = False

        while q:
            curr = q.popleft()

            if self.isValid(curr):
                res.append(curr)
                found = True

            if found:
                continue

            for i in range(len(curr)):
                if curr[i] not in '()':
                    continue

                nxt = curr[:i] + curr[i+1:]

                if nxt not in visited:
                    visited.add(nxt)
                    q.append(nxt)

        return sorted(list(set(res)))
