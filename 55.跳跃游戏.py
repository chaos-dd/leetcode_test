#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        end = 0
        for i in range(len(nums)):
            if end < i:
                return False
            end = max(end, i+nums[i])
            if end >= len(nums)-1:
                return True
        # return end >= len(nums)-1



# @lc code=end

