#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums = sorted(nums)
        res = []
        for i in range(n):
            if i > 0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1, n):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                l, r = j + 1, n -1
                while l < r:
                    if l > j + 1 and nums[l] == nums[l-1]:
                        l += 1
                        continue
                    sum = nums[i]+nums[j]+nums[l]+nums[r]
                    if sum == target:
                        res.append((nums[i], nums[j], nums[l], nums[r]))
                        l += 1
                        r -= 1
                    elif sum < target:
                        l += 1
                    else:
                        r -= 1
        return res


# @lc code=end

