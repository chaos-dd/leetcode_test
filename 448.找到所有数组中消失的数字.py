#
# @lc app=leetcode.cn id=448 lang=python3
#
# [448] 找到所有数组中消失的数字
#

# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        for x in nums:
            val = x
            while nums[val-1] != val:
                tmp = nums[val-1]
                nums[val-1]=val
                val = tmp
        for i in range(len(nums)):
            if nums[i]!=i+1:
                ans.append(i+1)
        return ans

        
# @lc code=end

