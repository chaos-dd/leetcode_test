#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子数组
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = float('-inf')
        max_prod, min_prod = 1, 1
        for v in nums:
            ls = [v, max_prod*v, min_prod*v]
            max_prod = max(ls)
            min_prod = min(ls)
            ans=max(ans, max_prod)
        return ans
        
# @lc code=end

