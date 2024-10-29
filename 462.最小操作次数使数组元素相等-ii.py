#
# @lc app=leetcode.cn id=462 lang=python3
#
# [462] 最小操作次数使数组元素相等 II
#

# @lc code=start
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        def method1():
            nums2 = sorted(nums)
            mid = nums2[len(nums)//2]
            # print(mid)
            res = 0
            for v in nums:
                res += abs(v - mid)
            return res
        def method2():

            def partition(nums, l, r):
                key = nums[l]
                while l < r:
                    while l < r and nums[r] >= key:
                        r -= 1
                    nums[l] = nums[r]
                    while l < r and nums[l] <= key:
                        l += 1
                    nums[r] = nums[l]
                nums[l] = key
                return l
            
            n = len(nums)
            l, r = 0, n-1
            pos = partition(nums, l, r)
            # print(nums, pos)
            k = n//2
            while pos != k:
                if pos > k:
                    r = pos - 1
                else:
                    l = pos + 1
                if l <= r:
                    pos = partition(nums, l, r)

            mid = nums[k]
            # print(mid)
            res = 0
            for v in nums:
                res += abs(v - mid)
            return res
        return method2()

# @lc code=end

