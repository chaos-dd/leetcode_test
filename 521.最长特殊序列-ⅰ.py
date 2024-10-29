#
# @lc app=leetcode.cn id=521 lang=python3
#
# [521] 最长特殊序列 Ⅰ
#

# @lc code=start
class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        s1 = a if len(a)>= len(b) else b
        s2 = a if len(a)< len(b) else b
        dup = set(s2)
        ans = []
        for c in s1:
            if c not in dup:
                ans.append(c)
        return len(ans) if len(ans)>0 else -1
        
# @lc code=end

