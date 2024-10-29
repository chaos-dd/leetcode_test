#
# @lc app=leetcode.cn id=934 lang=python3
#
# [934] 最短的桥
#

# @lc code=start
from collections import deque
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        island1 = []

        def dfs(r, c):
            if not (0<=r<n and 0<=c<n):
                return
            if grid[r][c] == 0:
                return
            if grid[r][c] == -1:
                return
            grid[r][c] = -1
            # print('debug', r, c)
            island1.append((r, c))
            for nr, nc in [[r+1,c],[r-1,c],[r,c+1], [r,c-1]]:
                # print(nr, nc)
                dfs(nr, nc)

        for r in range(n):
            for c in range(n):
                dfs(r,c)
                if len(island1) != 0:
                    break
            if len(island1) != 0:
                break
        
        # print(island1)
        # print(grid)
        q = island1
        res = 0
        while len(q) != 0:
            lastq = q#bfs切换两个本次队列和上次队列
            q = []
            for (r, c) in lastq:
                for nr, nc in [[r+1,c],[r-1,c],[r,c+1], [r,c-1]]:
                    if 0<=nr<n and 0<=nc<n:
                        if grid[nr][nc] == 1:
                            # print(r,c, nr, nc)
                            return res
                        if grid[nr][nc] == 0:
                            grid[nr][nc] = -1#访问过的不在访问
                            q.append((nr, nc))
            res += 1
        return res
            
# @lc code=end

