#
# @lc app=leetcode.cn id=442 lang=python3
#
# [442] 数组中重复的数据
#

# @lc code=start
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        for idx in range(len(nums)):
            while True:
                val = nums[idx]
                if nums[val-1]==val:
                    break
                nums[val-1], nums[idx]=nums[idx], nums[val-1]
        ans = []
        for idx in range(len(nums)):
            if nums[idx] != idx + 1:
                ans.append(nums[idx])
        return ans
        
# @lc code=end

