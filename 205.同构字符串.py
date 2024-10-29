#
# @lc app=leetcode.cn id=205 lang=python3
#
# [205] 同构字符串
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dic1, dic2 = {}, {}
        for i in range(len(s)):
            if s[i] not in dic1:
                dic1[s[i]] = t[i]
            if t[i] not in dic2:
                dic2[t[i]] = s[i]
            if dic1[s[i]] != t[i] or dic2[t[i]] != s[i]:
                return False
        return True
            

# @lc code=end

