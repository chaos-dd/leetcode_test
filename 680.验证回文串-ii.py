#
# @lc app=leetcode.cn id=680 lang=python3
#
# [680] 验证回文串 II
#

# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPali(s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return isPali(s, l + 1, r) or isPali(s, l, r - 1)
        return True

# @lc code=end

