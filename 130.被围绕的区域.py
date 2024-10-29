#
# @lc app=leetcode.cn id=130 lang=python3
#
# [130] 被围绕的区域
#

# @lc code=start
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def method1():
            m, n = len(board), len(board[0])

            def dfs(r, c):
                board[r][c] = 'A'
                for nr, nc in [[r+1, c], [r-1,c], [r, c+1], [r, c-1]]:
                    if 0<=nr<m and 0<=nc<n and board[nr][nc] == 'O':
                        dfs(nr, nc)
            for i in range(m):
                if board[i][0] == 'O':
                    dfs(i, 0)
                if board[i][n-1] == 'O':
                    dfs(i, n-1)
            for i in range(n):
                if board[0][i] == 'O':
                    dfs(0, i)
                if board[m-1][i] == 'O':
                    dfs(m-1, i)
            for r in range(m):
                for c in range(n):
                    if board[r][c] == 'O':
                        board[r][c] = 'X'
                    elif board[r][c] == 'A':
                        board[r][c] = 'O'
                
        def method2():
            nonlocal board
            m, n = len(board), len(board[0])

            def dfs(r, c):
                if board[r][c] != 'O':
                    return
                board[r][c] = 'A'
                for nr, nc in [[r+1,c], [r-1,c], [r, c+1], [r,c-1]]:
                    if 0<=nr<m and 0<=nc<n and board[nr][nc] == 'O':
                        dfs(nr, nc)
            for i in range(m):
                dfs(i, 0)
                dfs(i, n-1)
            for i in range(n):
                dfs(0, i)
                dfs(m-1,i)
            for r in range(m):
                for c in range(n):
                    if board[r][c] == 'A':
                        board[r][c] = 'O'
                    elif board[r][c] == 'O':
                        board[r][c] = 'X'
        
        def method3():
            m, n = len(board), len(board[0])
            parent = [i for i in range(m*n)]
            size = parent[:]
            def find(i):
                while parent[i] != i:
                    parent[i] = parent[parent[i]]
                    i = parent[i]
                return i
            def union(i, j):
                pi, pj = find(i), find(j)
                if pi != pj:
                    if size[pi] < size[pj]:
                        size[pj] += size[pi]
                        parent[pi] = pj
                    else:
                        size[pi] += size[pj]
                        parent[pi] = pi
            def add(r, c):
                if board[r][c] != 'O':
                    return
                board[r][c] = 'A'
                for nr, nc in [[r+1,c], [r-1, c], [r, c+1], [r, c-1]]:
                    if 0<=nr<m and 0<=nc<n and board[nr][nc] == 'O':
                        union(r*n+c, nr*n+nc)
                        add(nr, nc) 
            for r in range(m):
                add(r,0)
                add(r,n-1)
            for c in range(n):
                add(0, c)
                add(m-1,c)
            for r in range(m):



        method3()
                        
# @lc code=end

