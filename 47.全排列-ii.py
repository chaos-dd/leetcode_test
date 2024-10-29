#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        ans = []
        cur = []
        flag = [0]*n
        def dfs(idx):
            if idx >= n:
                ans.append(cur[:])
                return
            for j in range(n):
                if j >0 and nums[j]==nums[j-1] and flag[j-1]==0:
                    continue
                if flag[j]==0:
                    flag[j]=1
                    cur.append(nums[j])
                    dfs(idx+1)
                    cur.pop()
                    flag[j]=0
        dfs(0)
        return ans
            
# @lc code=end

