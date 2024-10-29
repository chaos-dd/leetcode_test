#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = 0
        n = len(nums)
        nums = sorted(nums)
        diff = float('inf')
        for i in range(n):
            l, r = i+1, n-1
            while l < r:
                sum = nums[i]+nums[l]+nums[r]
                if abs(target-sum) < diff:
                    diff = abs(target-sum)
                    res = sum
                if sum == target:
                    return res
                elif sum < target:
                    l += 1
                else:
                    r -= 1
        return res
                
# @lc code=end

