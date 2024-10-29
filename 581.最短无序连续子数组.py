#
# @lc app=leetcode.cn id=581 lang=python3
#
# [581] 最短无序连续子数组
#

# @lc code=start
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        right_min = float('inf')
        n=len(nums)
        left = len(nums)-1
        for i in range(n-1,-1,-1):
            if nums[i]>right_min:
                left = i
            right_min = min(right_min, nums[i])
        right = 0
        left_max = float('-inf')
        for i in range(n):
            if nums[i]<left_max:
                right = i
            left_max = max(left_max, nums[i])
        return right-left+1 if right>left else 0

        
# @lc code=end

