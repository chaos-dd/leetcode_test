#
# @lc app=leetcode.cn id=217 lang=python3
#
# [217] 存在重复元素
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mem = set()
        for v in nums:
            if v in mem:
                return True
            mem.add(v)
        return False
    
# @lc code=end

