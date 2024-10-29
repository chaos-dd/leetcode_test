#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        cur = []
        def dfs(idx, target):
            if target<0:
                return
            if target == 0:
                ans.append(cur[:])
                return
            if idx == len(candidates):
                return
            cur.append(candidates[idx])
            dfs(idx,target-candidates[idx])
            cur.pop()
            dfs(idx+1,target)
        dfs(0, target)
        return ans

# @lc code=end

