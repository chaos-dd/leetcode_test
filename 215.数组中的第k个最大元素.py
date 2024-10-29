#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#

# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def method1():
            import heapq
            hp = []
            for i in range(k):
                heapq.heappush(hp, nums[i])
            for i in range(k, len(nums)):
                if nums[i]>hp[0]:
                    heapq.heappop(hp)
                    heapq.heappush(hp, nums[i])
            return hp[0]
        def method2():
            import random
            def partition(l, r):
                idx = random.randint(l,r)
                nums[l],nums[idx]=nums[idx],nums[l]
                key=nums[l]
                while l < r:
                    while l < r and nums[r]>=key:
                        r -= 1
                    nums[l]=nums[r]
                    while l < r and nums[l]<=key:
                        l += 1
                    nums[r]=nums[l]
                nums[l]=key
                return l

            l, r = 0, len(nums)-1
            pos = partition(l, r)
            target = len(nums)-k
            while pos != target:
                if pos < target:
                    l = pos + 1
                else:
                    r = pos - 1
                pos = partition(l, r)
            return nums[pos]
        return method2()

        
# @lc code=end

