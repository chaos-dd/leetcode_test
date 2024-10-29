#
# @lc app=leetcode.cn id=188 lang=python3
#
# [188] 买卖股票的最佳时机 IV
#

# @lc code=start
from functools import cache
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:

        @cache
        def dfs(idx, st, k):
            if k == 0:
                return 0
            if idx >= len(prices):
                return 0
            t1 = dfs(idx+1, 1, k) - prices[idx] if st == 0 else 0
            t2 = dfs(idx+1, 0, k - 1) + prices[idx] if st == 1 else 0
            t3 = dfs(idx+1, st, k)
            return max([t1, t2, t3])
        

        return dfs(0, 0, k)


# @lc code=end

