#
# @lc app=leetcode.cn id=268 lang=python3
#
# [268] 丢失的数字
#

# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum = n *(n+1)//2
        for v in nums:
            sum -= v
        return sum
# @lc code=end

