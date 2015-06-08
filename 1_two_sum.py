class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        num = zip(nums, range(len(nums)))
        num.sort();
        i = 0
        j = len(nums) - 1
        while  i < j:
            sum = num[i][0] + num[j][0]
            if sum < target:
                i += 1
            elif sum > target:
                j -= 1
            else:
                idx1 = num[i][1]
                idx2 = num[j][1]
                if idx1 > idx2:
                    idx1,idx2 = idx2, idx1
                return [idx1 + 1, idx2 + 1]
