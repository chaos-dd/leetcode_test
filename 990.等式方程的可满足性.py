#
# @lc app=leetcode.cn id=990 lang=python3
#
# [990] 等式方程的可满足性
#

# @lc code=start
from typing import List


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        def method1():
            parent = [i for i in range(26)]
            def find(i):
                if parent[i] != i:
                    parent[i] = find(parent[i])
                return parent[i]
            def union(i, j):
                parent[find(i)] = find(j)
            for eq in equations:
                if eq[1] != '=':
                    continue
                idx1 = ord(eq[0]) - ord('a')
                idx2 = ord(eq[3]) - ord('a')
                union(idx1, idx2)

            for eq in equations:
                if eq[1] != '!':
                    continue
                idx1 = ord(eq[0]) - ord('a')
                idx2 = ord(eq[3]) - ord('a')
                if find(idx1) == find(idx2):
                    return False
            return True

        return method1()

# ss = Solution()
# print(ss.equationsPossible(["a==b","b!=a"]))
# @lc code=end

