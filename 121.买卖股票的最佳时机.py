#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        minv=prices[0]
        for i in range(1, len(prices)):
            ans = max(ans, prices[i]-minv)
            minv = min(minv, prices[i])
        return ans
        
# @lc code=end

