#
# @lc app=leetcode.cn id=714 lang=python3
#
# [714] 买卖股票的最佳时机含手续费
#

# @lc code=start
from functools import cache
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:

        def method1():
            @cache
            def dfs(idx, st):
                if idx >= len(prices):
                    return 0

                n1 = dfs(idx+1, 0) + prices[idx] if st == 1 else 0
                n2 = dfs(idx+1, 1) - prices[idx] -fee if st == 0 else 0
                n3 = dfs(idx+1, st)
                return max([n1,n2,n3])
            return dfs(0, 0)
        def method2():
            #固定套路
            n = len(prices)
            dp = [[0, 0] for _ in range(n)]
            dp[0][1] = -prices[0] - fee
            for i in range(1, n):
                dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
                dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i] - fee)
            return dp[-1][0]
        return method2()

# @lc code=end

