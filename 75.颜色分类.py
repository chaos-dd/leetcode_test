#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right=0,len(nums)-1
        for i in range(len(nums)):
            while i<=right and nums[i] == 2:
                nums[i],nums[right]=nums[right],nums[i]
                right -= 1
            if nums[i]==0:
                nums[i],nums[left]=nums[left],nums[i]
                left += 1
                

# @lc code=end

