#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子数组和
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = float('-inf')
        sum = 0
        for v in nums:
            sum += v
            ans = max(ans, sum)
            sum = max(sum, 0)
        return ans
# @lc code=end

