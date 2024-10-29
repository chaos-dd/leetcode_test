#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def bt(i, flag):
            if i >= len(nums):
                res.append(cur[:])
                return
            bt(i + 1, True)
            if flag and i > 0 and nums[i] == nums[i-1]:
                return
            cur.append(nums[i])
            bt(i + 1, False)
            cur.pop()
        res = []
        cur = []
        nums = sorted(nums)
        bt(0, True)
        return res

# @lc code=end

