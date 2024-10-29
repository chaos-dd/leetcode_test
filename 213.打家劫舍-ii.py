#
# @lc app=leetcode.cn id=213 lang=python3
#
# [213] 打家劫舍 II
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        def method1():
            def inner(s, e):
                if s > e :
                    return 0
                d0, d1 = 0, nums[s]
                for i in range(s + 1, e+1):
                    d3 = max(d0 + nums[i], d1)
                    d0, d1 = d1, d3
                return d1
            if len(nums) == 0:
                return 0
            elif len(nums) == 1:
                return nums[0]
            
            #第一个抢了最后一个就不能抢就是0-n-2
            #第一个不抢，就是1至n-1
            return max([inner(0, len(nums)-2), inner(1, len(nums)-1)])
        def method2():
            from functools import cache

            n = len(nums)
            @cache
            def dfs(i, st0, st):
                if i >= n:
                    return 0
                if i == n-1:
                    if st0 == 0 and st == 0:
                        return nums[i]
                    else:
                        return 0
                elif i == 0:
                    if st0 == 0:
                        return dfs(i+1, st0, 0)
                    else:
                        return dfs(i+1, st0, 1) + nums[i]
                else:
                    n1 = dfs(i+1, st0, 1) + nums[i] if st == 0 else 0
                    n2 = dfs(i+1, st0, 0) if st == 1 else 0
                    n3 = dfs(i+1, st0, 0)
                    return max([n1, n2, n3])
            n1 = dfs(0,0,0)
            n2 = dfs(0, 1, 0)
            # print(n1, n2)
            return max([n1, n2])
        return method2()

# @lc code=end

