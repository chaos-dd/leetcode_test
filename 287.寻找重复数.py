#
# @lc app=leetcode.cn id=287 lang=python3
#
# [287] 寻找重复数
#

# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 1, n-1
        while l <= r:
            m=(l+r)//2
            cnt = 0
            for x in nums:
                if x <= m:
                    cnt += 1
            if cnt <= m:
                l = m + 1
            else:
                r = m - 1
        return l
        
# @lc code=end

