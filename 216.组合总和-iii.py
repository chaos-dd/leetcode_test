#
# @lc app=leetcode.cn id=216 lang=python3
#
# [216] 组合总和 III
#

# @lc code=start
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        cur = []
        def bt(i, sum):
            if sum == 0 and len(cur) == k:
                res.append(cur[:])
                return
            if sum < 0:
                return
            if i > 9:
                return
            cur.append(i)
            bt(i+1,sum-i)
            cur.pop()
            bt(i+1,sum)
        bt(1, n)
        return res
            
# @lc code=end

