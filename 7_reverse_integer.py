class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        if x >= 0:
            res = int(str(x)[::-1])
        else:
            res = int('-'+str(x)[-1:0:-1])
        return res if res <= 2147483647 and res>=-2147483648 else 0
