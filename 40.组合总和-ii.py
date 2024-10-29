#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates=sorted(candidates)
        ans = []
        cur = []
        def dfs(idx, target, last):
            if target < 0:
                return
            if target==0:
                ans.append(cur[:])
                return
            if idx == len(candidates):
                return
            if last == -1 or last != candidates[idx]:
                cur.append(candidates[idx])
                dfs(idx+1, target-candidates[idx], last)
                cur.pop()
            dfs(idx+1, target, candidates[idx])
        dfs(0, target, -1)
        return ans

# @lc code=end

