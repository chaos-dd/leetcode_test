#
# @lc app=leetcode.cn id=260 lang=python3
#
# [260] 只出现一次的数字 III
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xs = 0
        for v in nums:
            xs = xs ^ v
        lb = xs & (-xs)
        ans = [0,0]
        for v in nums:
            if lb & v == 0:
                ans[0] ^= v
            else:
                ans[1] ^= v
        return ans

# @lc code=end

