#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        i = 0
        flag = True
        while flag:
            if i >= len(strs[0]):
                break
            c = strs[0][i]
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or strs[j][i] != c:
                    flag = False
                    break
            if flag:
                i += 1
        return strs[0][0:i]

            

   
# @lc code=end

