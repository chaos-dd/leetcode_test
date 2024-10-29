#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def method1():
            n=len(nums)
            ans = []
            cur = []
            flag = [0]*n
            def dfs(idx):
                if idx >= n:
                    ans.append(cur[:])
                    return
                for j in range(n):
                    if flag[j] == 0:
                        flag[j]=1
                        cur.append(nums[j])
                        dfs(idx+1)
                        flag[j]=0
                        cur.pop()
            dfs(0)
            return ans
        def method2():
            n=len(nums)
            ans = []
            cur = [0]*n
            flag = [0]*n
            #每个数字
            def dfs(idx):
                if idx >=n:
                    ans.append(cur[:])
                    return
                for j in range(n):
                    if flag[j]==0:
                        flag[j]=1
                        cur[j]=nums[idx]
                        dfs(idx+1)
                        flag[j]=0
            dfs(0)
            return ans
        def method3():
            n=len(nums)
            ans = []
            cur = [None]*n
            #每个数字
            def dfs(idx):
                if idx >=n:
                    ans.append(cur[:])
                    return
                for j in range(n):
                    if cur[j] is None:
                        cur[j]=nums[idx]
                        dfs(idx+1)
                        cur[j]=None
            dfs(0)
            return ans

        return method4()

# @lc code=end

