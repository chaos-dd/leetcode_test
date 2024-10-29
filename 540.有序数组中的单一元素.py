#
# @lc app=leetcode.cn id=540 lang=python3
#
# [540] 有序数组中的单一元素
#

# @lc code=start
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        def method1():
            l, r = 0, len(nums)-1
            s = 0
            while l <= r:
                s ^= nums[l]
                l += 1
            return s
        def method2():
            i = 0
            while i < len(nums) - 2:
                if nums[i] != nums[i+1]:
                    return nums[i]
                i += 2
            return nums[i]
        def method3():
            l, r = 0, len(nums)-1
            while l < r:#l=r时就一个值直接返回
                m = (l+r)//2
                if m % 2 == 0:#偶数和后一个比
                    if nums[m] == nums[m+1]:
                        l = m + 1
                    else:
                        r = m
                else:#奇数和前一个比
                    if nums[m] == nums[m-1]:
                        l = m + 1
                    else:
                        r = m - 1# r=m也行
            return nums[r]
        def method4():
            l, r = 0, len(nums)-1
            while l < r:
                m = (l+r)//2
                #偶数m^1=m+1 奇数m^1=m-1
                if nums[m] == nums[m^1]:
                    l = m + 1
                else:
                    r = m
            return nums[r]

        return method4()
            
# @lc code=end

