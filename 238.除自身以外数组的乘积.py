#
# @lc app=leetcode.cn id=238 lang=python3
#
# [238] 除自身以外数组的乘积
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans = [1]*n
        prod = 1
        for i in range(n):
            ans[i] = prod
            prod*=nums[i]
        prod = 1
        for i in range(n-1,-1,-1):
            ans[i] *= prod
            prod*=nums[i]
        return ans

        
# @lc code=end

