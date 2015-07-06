class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        l = [(val, idx) for idx,val in enumerate(nums)]
        l.sort()
        i = 1
        while i < len(l):
            if l[i][0] == l[i-1][0] and abs(l[i][1] - l[i-1][1]) <= k:
                return True
            i += 1
        return False

l = [1,2,3,4,1]
print Solution().containsNearbyDuplicate(l, 5)
