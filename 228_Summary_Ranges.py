class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        i = 0
        j = 0
        res = []
        while j < len(nums):
            if nums[j] - nums[i] == j - i:
                j += 1
            else:
                res.append(str(nums[i]))
                if j - i > 1:
                    res[-1] += "->" + str(nums[j - 1])
                i = j
        if len(nums) > 0:
            res.append(str(nums[i]))
            if j - i > 1:
                res[-1] += "->" + str(nums[j - 1])
        return res

# print Solution().summaryRanges([0, 1, 2, 4, 5, 7])
print Solution().summaryRanges([])
