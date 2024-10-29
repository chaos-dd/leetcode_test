#
# @lc app=leetcode.cn id=542 lang=python3
#
# [542] 01 矩阵
#

# @lc code=start
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        res = [[float('inf')]*n for _ in range(m)]

        def method1():
            for r in range(m):
                for c in range(n):
                    if mat[r][c] == 0:
                        res[r][c] = 0
                    else:
                        if r > 0:
                            res[r][c] = min(res[r][c], res[r-1][c]+1)
                        if c > 0:
                            res[r][c] = min(res[r][c], res[r][c-1]+1)
            for r in reversed(range(m)):
                for c in reversed(range(n)):
                    if mat[r][c] == 0:
                        continue
                    if r < m -1:
                        res[r][c] = min(res[r][c], res[r+1][c]+1)
                    if c < n - 1:
                        res[r][c] = min(res[r][c], res[r][c+1]+1)
            return res

        def method2():
            from collections import deque
            q = deque()

            for r in range(m):
                for c in range(n):
                    if mat[r][c] == 0:
                        res[r][c] = 0
                        q.append((r,c))

            # while len(q) != 0:
            #     cnt = len(q)
            #     while cnt > 0:
            #         cnt -= 1
            #         (r, c) = q.popleft()
            #         for nr, nc in [[r-1,c], [r+1,c], [r,c+1], [r,c-1]]:
            #             if 0<=nr<m and 0<=nc<n and res[nr][nc] == float('inf'):
            #                 res[nr][nc] = res[r][c] + 1
            #                 q.append((nr,nc))
                        # while len(q) != 0:
            while len(q) != 0:
                (r, c) = q.popleft()
                for nr, nc in [[r-1,c], [r+1,c], [r,c+1], [r,c-1]]:
                    if 0<=nr<m and 0<=nc<n and res[nr][nc] == float('inf'):
                        res[nr][nc] = res[r][c] + 1
                        q.append((nr,nc))

            return res
        return method2()

# @lc code=end

