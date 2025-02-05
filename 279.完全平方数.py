#
# @lc app=leetcode.cn id=279 lang=python3
#
# [279] 完全平方数
#

# @lc code=start
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')]*(n+1)
        dp[0]=0
        for i in range(1, n+1):
            for j in range(1, int(i**0.5)+1):
                if i-j*j>=0:
                    dp[i] = min(dp[i], dp[i-j*j]+1)
        return dp[-1]
        
# @lc code=end

