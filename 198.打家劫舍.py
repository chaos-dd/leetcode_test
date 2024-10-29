#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp = [0]*n
        for i in range(n):
            if i == 0:
                dp[i]=nums[0]
            elif i == 1:
                dp[i]=max(nums[0],nums[1])
            else:
                dp[i]=max(dp[i-2]+nums[i], dp[i-1])
        return dp[-1]
        
# @lc code=end

