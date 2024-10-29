#
# @lc app=leetcode.cn id=123 lang=python3
#
# [123] 买卖股票的最佳时机 III
#

# @lc code=start
from functools import cache

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        def method2():
            @cache
            def dfs(i, j, k):
                #第i天，j=1有股票，k还有多少次卖的机会
                if k == 0:
                    return 0
                if i >= len(prices):
                    return 0
                #手上有股票卖出
                t1 = dfs(i+1, 0, k-1) + prices[i] if j == 1 else 0
                #手上没股票买入
                t2 = dfs(i+1, 1, k) - prices[i] if j == 0 else 0
                #不操作
                t3 = dfs(i+1, j, k)
                return max([t1, t2,t3])
            return dfs(0, 0, 2)
        return method2()
# @lc code=end

