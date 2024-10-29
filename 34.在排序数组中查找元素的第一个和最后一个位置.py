#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search(l, r, lower):
            while l <= r:
                m = (l+r)//2
                if nums[m] == target:
                    if lower:
                        r = m - 1
                    else:
                        l = m + 1
                elif nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return l
        left = search(0, len(nums)-1, True)
        right = search(0, len(nums)-1, False) - 1
        return [left, right] if left<=right else [-1,-1]
        

            

# @lc code=end

