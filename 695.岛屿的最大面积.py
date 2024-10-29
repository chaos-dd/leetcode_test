#
# @lc app=leetcode.cn id=695 lang=python3
#
# [695] 岛屿的最大面积
#

# @lc code=start
from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def method1():
            def dfs(grid, i, j):
                if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                    return 0
                if grid[i][j] == 0:
                    return 0
                grid[i][j] = 0
                return 1 + dfs(grid, i, j-1) + dfs(grid, i, j+1) + dfs(grid, i-1, j) + dfs(grid, i+1, j)
            
            res = 0
            for r in range(len(grid)):
                for c in range(len(grid[0])):
                    res = max(res, dfs(grid, r,c))
            return res

        def method2():
            if len(grid)<=0:
                return 0
            m, n = len(grid), len(grid[0])
            def dfs(r, c):
                if grid[r][c] != 1:
                    return 0
                res = 1
                grid[r][c] = 2
                for nr, nc in [[r-1,c],[r+1,c],[r,c+1],[r,c-1]]:
                    if 0<=nr<m and 0<=nc<n and grid[nr][nc] == 1:
                        res += dfs(nr, nc)
                return res
            res = 0
            for r in range(m):
                for c in range(n):
                    if grid[r][c] != 1:
                        continue
                    res = max(res, dfs(r,c))
            return res


        def method3():
            if len(grid)<=0:
                return 0
            m,n = len(grid), len(grid[0])
            parent = [-1]*(m*n)
            size = [1]*(m*n)
            for r in range(m):
                for c in range(n):
                    if grid[r][c] == 1:
                        parent[r*n+c] = r*n+c
            def find(i):
                while parent[i] != i:
                    parent[i] = parent[parent[i]]
                    i = parent[i]
                return i
            def union(i,j):
                pi, pj = find(i), find(j)
                if pi != pj:
                    if size[pi] < size[pj]:
                        size[pj] += size[pi]
                        parent[pi] = pj
                    else:
                        size[pi] += size[pj]
                        parent[pj] = pi
            for r in range(m):
                for c in range(n):
                    if grid[r][c] != 1:
                        continue
                    for nr, nc in [[r-1,c],[r+1,c],[r,c+1],[r,c-1]]:
                        if 0<=nr<m and 0<=nc<n and grid[nr][nc] == 1:
                            union(r*n+c, nr*n+nc)
            # print(parent)
            # print(size)
            res = 0
            for r in range(m):
                for c in range(n):
                    if parent[r*n+c] == r*n+c:
                        res = max(res, size[r*n+c])
            return res
            
        return method3()



# @lc code=end

