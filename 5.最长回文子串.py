#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check(i, j):
            while i >= 0 and j <len(s) and s[i]==s[j]:
                i-=1
                j+=1
            return i+1, j-1
        res = ''
        for i in range(len(s)):
            l,r = check(i, i)
            if r-l+1 > len(res):
                res=s[l:r+1]
            l,r = check(i, i+1)
            if r-l+1 > len(res):
                res=s[l:r+1]
        return res

# @lc code=end

