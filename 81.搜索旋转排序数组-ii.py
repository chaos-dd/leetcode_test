#
# @lc app=leetcode.cn id=81 lang=python3
#
# [81] 搜索旋转排序数组 II
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # l, r = 0, len(nums)-1
        # while l <= r:
        #     m = (l+r)//2
        #     if nums[m] == target:
        #         return True
        #     elif nums[l]<nums[m]:
        #         if nums[l]<=target<nums[m]:
        #             r = m - 1
        #         else:
        #             l = m + 1
        #     elif nums[l]==nums[m]:
        #         l += 1
        #     else:
        #         if nums[m]<target<=nums[r]:
        #             l = m + 1
        #         else:
        #             r = m - 1
        # return False
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return True
            if nums[l] == nums[mid] and nums[mid] == nums[r]:
                l += 1
                r -= 1
            elif nums[l] <= nums[mid]:
                if nums[l] <= target and target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        
        return False
        
# @lc code=end

