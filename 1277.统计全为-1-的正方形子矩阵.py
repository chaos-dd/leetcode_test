#
# @lc app=leetcode.cn id=1277 lang=python3
#
# [1277] 统计全为 1 的正方形子矩阵
#

# @lc code=start
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m,n=len(matrix),len(matrix[0])
        dp=[[0]*n for _ in range(m)]
        ans = 0
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 1:
                    if r==0 or c == 0:
                        dp[r][c]=1
                    else:
                        dp[r][c]=min(dp[r-1][c],dp[r-1][c-1],dp[r][c-1])+1
                    ans += dp[r][c]
        return ans
        
# @lc code=end

