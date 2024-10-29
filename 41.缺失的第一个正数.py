#
# @lc app=leetcode.cn id=41 lang=python3
#
# [41] 缺失的第一个正数
#

# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        def method1():
            dup = set(nums)
            for i in range(1,max(2,max(nums)+2)):
                if i not in dup:
                    return i
        def method2():
            n=len(nums)
            for i in range(n):
                while 1<=nums[i]<=n and nums[nums[i]-1] != nums[i]:
                    nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
                    #错误，nums[i]已经改了
                    #nums[i], nums[nums[i]-1] = nums[nums[i]-1], nums[i]
            for i in range(n):
                if nums[i] - 1 != i:
                    return i + 1
            return n + 1

        return method2()
        
# @lc code=end

