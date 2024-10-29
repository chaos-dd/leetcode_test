#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)
        n=len(nums)
        ans = []
        for i in range(n):
            #关键
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i + 1, n-1
            while l < r:
                #关键
                if l > i + 1 and nums[l] == nums[l-1]:
                    l += 1
                    continue
                sum=nums[i]+nums[l]+nums[r]
                if sum == 0:
                    ans.append((nums[i],nums[l],nums[r]))
                    l += 1
                    r -= 1
                elif sum < 0:
                    l += 1
                else:
                    r -= 1
        return ans

# @lc code=end

