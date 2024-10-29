#
# @lc app=leetcode.cn id=345 lang=python3
#
# [345] 反转字符串中的元音字母
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        mem = set(['a', 'e', 'i','o', 'u',
                   'A', 'E', 'I','O', 'U'])
        l, r = 0, len(s)-1
        out = [c for c in s]
        while l < r:
            while l < r and out[l] not in mem:
                l += 1
            while l < r and out[r] not in mem:
                r -= 1
            out[l], out[r] = out[r], out[l]
            l += 1
            r -= 1
        return ''.join(out)
# @lc code=end

