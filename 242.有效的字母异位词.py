#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dic = {}
        for c in s:
            if c not in dic:
                dic[c] = 0
            dic[c] += 1
        for c in t:
            if c not in dic or dic[c] == 0:
                return False
            dic[c] -= 1
        return True
# @lc code=end

