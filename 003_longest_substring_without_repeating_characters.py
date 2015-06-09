class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        pos = {}
        left = 0
        res = 0
        for i in range(len(s)):
            if pos.has_key(s[i]) and pos[s[i]] >= left:
                left = pos[s[i]] + 1
            pos[s[i]] = i
            res = max(res, i - left + 1)
        return res
