#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        cur = []
        def bt(i):
            if len(cur) == k:
                res.append(cur[:])
                return
            if i > n:
                return
            cur.append(i)
            bt(i+1)
            cur.pop()
            bt(i+1)
            
        def bt(i):
            if len(cur) == k:
                res.append(cur[:])
                return
            for j in range(i, n + 1):
                cur.append(j)
                bt(j+1)
                cur.pop()
        bt(1)
        return res


# @lc code=end

