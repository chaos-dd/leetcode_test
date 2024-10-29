#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        factor = 1
        ans = [[] for _ in range(numRows)]
        idx = 0
        for i in range(len(s)):
            ans[idx].append(s[i])
            idx += factor
            if idx % (numRows-1) == 0:
                factor = -factor
        return ''.join([''.join(r) for r in ans])

        
# @lc code=end

