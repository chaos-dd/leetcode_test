#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def method1():
            res = 0
            for i in range(1, len(prices)):
                if prices[i] > prices[i-1]:
                    res += prices[i]-prices[i-1]
            return res
        def method2():
            n = len(prices)
            dp = [[0,0] for _ in range(n)]
            dp[0][1] = -prices[0]
            for i in range(1, n):
                dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
                dp[i][1] = max(dp[i-1][0] - prices[i], dp[i-1][1])
            return dp[-1][0]
        return method2()


# @lc code=end

