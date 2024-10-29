#
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] 杨辉三角 II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        cur = [0]*(rowIndex+1)
        cur[0]=1
        for i in range(rowIndex+1):
            for j in range(i, 0, -1):
                cur[j] = cur[j-1] + cur[j]
        return cur

# @lc code=end

