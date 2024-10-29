#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n=len(grid),len(grid[0])
        def dfs(r, c):
            if grid[r][c] == '0':
                return 0
            grid[r][c] = '0'
            for nr, nc in [[r+1,c], [r-1,c], [r,c+1],[r,c-1]]:
                if 0<=nr<m and 0<=nc<n and grid[nr][nc]=='1':
                    dfs(nr,nc)
            return 1
        
        ans = 0
        for r in range(m):
            for c in range(n):
                ans += dfs(r, c)
        return ans

        
# @lc code=end

