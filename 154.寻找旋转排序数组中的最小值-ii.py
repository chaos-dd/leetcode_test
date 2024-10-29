#
# @lc app=leetcode.cn id=154 lang=python3
#
# [154] 寻找旋转排序数组中的最小值 II
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0,len(nums)-1
        while l < r:
            m=(l+r)//2
            if nums[m] == nums[r]:
                r = r - 1
            elif nums[m]<nums[r]:
                r = m
            else:
                l = l + 1
        return nums[l]
        
# @lc code=end

