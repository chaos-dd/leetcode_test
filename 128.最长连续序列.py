#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        def method1():
            mem = set(nums)
            ans = 0
            for v in nums:
                if v - 1 in mem:
                    continue
                x = v
                cur = 0
                while x in mem:
                    cur += 1
                    x += 1
                ans=max(ans,cur)
            return ans
        def method2():
            nonlocal nums
            if len(nums)==0:
                return 0
            nums = sorted(nums)
            ans = 1
            cur = 1
            for i in range(len(nums)-1):
                if nums[i] + 1 == nums[i+1]:
                    cur += 1
                elif nums[i] != nums[i+1]:
                    cur = 1
                ans = max(ans, cur)
            return ans
        return method2()
        
# @lc code=end

