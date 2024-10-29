#
# @lc app=leetcode.cn id=309 lang=python3
#
# [309] 买卖股票的最佳时机含冷冻期
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        hold = [0]*n
        sell = [0]*n
        cold = [0]*n
        hold[0]=-prices[0]
        for i in range(1, n):
            hold[i] = max(cold[i-1]-prices[i], hold[i-1])
            sell[i] = hold[i-1]+prices[i]
            cold[i] = max(sell[i-1], cold[i-1])
        return max(sell[-1], cold[-1])

        
# @lc code=end

