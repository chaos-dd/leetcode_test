#
# @lc app=leetcode.cn id=1631 lang=python3
#
# [1631] 最小体力消耗路径
#

# @lc code=start
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

        m,n=len(heights), len(heights[0])
        edges = []
        for r in range(m):
            for c in range(n):
                id0 = r*n+c
                if r < m -1:
                    edges.append((id0, id0+n, abs(heights[r][c]-heights[r+1][c])))
                if c < n -1:
                    edges.append((id0, id0+1, abs(heights[r][c]-heights[r][c+1])))
        parent = [i for i in range(m*n)]
        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]
        def union(i, j):
            parent[find(i)] = find(j)
        edges = sorted(edges, key=lambda x:x[2])
        for e in edges:
            union(e[0], e[1])
            if find(0) == find(m*n-1):
                return e[2]
        return 0

# @lc code=end

