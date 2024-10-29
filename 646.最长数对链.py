#
# @lc app=leetcode.cn id=646 lang=python3
#
# [646] 最长数对链
#

# @lc code=start
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        def method1():
            nonlocal pairs
            from functools import cache
            pairs = sorted(pairs, key=lambda x:(x[0], x[1]))

            @cache
            def dfs(i, j):
                if i == len(pairs):
                    return 0
                res = dfs(i+1, j)
                if j == -1 or pairs[j][1] < pairs[i][0]:
                    res = max(res, dfs(i+1, i)+1)
                return res
            return dfs(0, -1)

        def method2():
            nonlocal pairs
            pairs = sorted(pairs, key=lambda x:(x[0], x[1]))
            n = len(pairs)
            dp = [0] * n
            dp[0]=1
            for i in range(1, n):
                dp[i] = dp[i-1]
                for j in range(i):
                    if pairs[j][1] < pairs[i][0]:
                        dp[i] = max(dp[i], dp[j]+1)
            return dp[-1]
        def method3():
            nonlocal pairs
            import bisect
            pairs = sorted(pairs, key=lambda x:(x[0], x[1]))
            arr = []
            for (x, y) in pairs:
                i = bisect.bisect_left(arr, x)
                if i >= len(arr):
                    arr.append(y)
                else:
                    arr[i] = min(arr[i], y)
                # print(arr)
            return len(arr)
        def method4():
            nonlocal pairs
            pairs = sorted(pairs, key=lambda x:(x[1], x[0]))
            res = 1
            last = pairs[0][1]
            for i in range(1, len(pairs)):
                if pairs[i][0] > last:
                    res += 1
                    last = pairs[i][1]
            return res


        return method4()
# @lc code=end

