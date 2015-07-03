class Solution:
    # @param {integer[]} height
    # @return {integer}
    def maxArea(self, height):
        l = []
        for key, val in enumerate(height):
            l.append((val, key))
        l.sort(cmp=(lambda x, y: y[0]-x[0]))
        return self.solve(l)

    def solve(self, l):
        res = 0
        maxRight = -1
        for item in l:
            if maxRight > item[1]:
                res = max(res, item[0] * (maxRight - item[1]))
            maxRight = max(maxRight, item[1])
        maxLeft = len(l)
        for item in l:
            if maxLeft < item[1]:
                res = max(res, item[0] * (item[1] - maxLeft))
            maxLeft = min(maxLeft, item[1])
        return res
