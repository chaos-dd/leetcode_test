#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        last = nums[0]
        cnt = 1
        for i in range(1, len(nums)):
            if nums[i]==last:
                cnt += 1
            else:
                cnt -= 1
                if cnt == 0:
                    last = nums[i]
                    cnt = 1
        return last
        
# @lc code=end

