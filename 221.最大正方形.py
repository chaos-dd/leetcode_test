#
# @lc app=leetcode.cn id=221 lang=python3
#
# [221] 最大正方形
#

# @lc code=start
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m,n=len(matrix),len(matrix[0])
        dp=[[0]*n for _ in range(m)]
        ans = 0
        for r in range(m):
            for c in range(n):
                if matrix[r][c] != '1':
                    continue
                if r==0 or c == 0:
                    dp[r][c]=1
                else:
                    dp[r][c]=min(dp[r-1][c-1],dp[r][c-1], dp[r-1][c]) + 1
                ans = max(ans,dp[r][c])
        return ans ** 2
        
# @lc code=end

