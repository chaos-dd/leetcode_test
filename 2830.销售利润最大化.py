#
# @lc app=leetcode.cn id=2830 lang=python3
#
# [2830] 销售利润最大化
#

# @lc code=start
class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:

        groups = [[] for _ in range(n)]
        for of in offers:
            groups[of[1]].append([of[0], of[2]])

        dp = [0]*(n+1)
        for i in range(1, n+1):
            dp[i]=dp[i-1]
            for start, gold in groups[i-1]:
                dp[i]=max(dp[i], dp[start]+gold)
        return dp[-1]

# @lc code=end

