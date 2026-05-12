from math import gcd

class Solution:
    def RangeLCMQuery(self, arr, queries):
        n = len(arr)

        # Function to calculate LCM
        def lcm(a, b):
            return (a * b) // gcd(a, b)

        # Segment Tree
        seg = [1] * (4 * n)

        # Build tree
        def build(idx, low, high):
            if low == high:
                seg[idx] = arr[low]
                return

            mid = (low + high) // 2
            build(2 * idx + 1, low, mid)
            build(2 * idx + 2, mid + 1, high)

            seg[idx] = lcm(seg[2 * idx + 1], seg[2 * idx + 2])

        # Update query
        def update(idx, low, high, pos, val):
            if low == high:
                seg[idx] = val
                return

            mid = (low + high) // 2

            if pos <= mid:
                update(2 * idx + 1, low, mid, pos, val)
            else:
                update(2 * idx + 2, mid + 1, high, pos, val)

            seg[idx] = lcm(seg[2 * idx + 1], seg[2 * idx + 2])

        # Range LCM query
        def query(idx, low, high, l, r):
            if r < low or high < l:
                return 1

            if l <= low and high <= r:
                return seg[idx]

            mid = (low + high) // 2

            left = query(2 * idx + 1, low, mid, l, r)
            right = query(2 * idx + 2, mid + 1, high, l, r)

            return lcm(left, right)

        build(0, 0, n - 1)

        ans = []

        for q in queries:
            if q[0] == 1:
                _, index, value = q
                arr[index] = value
                update(0, 0, n - 1, index, value)

            else:
                _, L, R = q
                ans.append(query(0, 0, n - 1, L, R))

        return ans
