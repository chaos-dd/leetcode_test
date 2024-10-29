#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def method1():
            ans = []
            cur = []
            def dfs(idx):
                if idx >= len(nums):
                    ans.append(cur[:])
                    return
                dfs(idx+1)
                cur.append(nums[idx])
                dfs(idx+1)
                cur.pop()
            dfs(0)
            return ans
        def method2():
            n = len(nums)
            ans = []
            for mask in range(2**n):
                cur = []
                for i in range(n):
                    if mask & (1<<i) != 0:
                        cur.append(nums[i])
                ans.append(cur)
            return ans
        return method1()
# @lc code=end

