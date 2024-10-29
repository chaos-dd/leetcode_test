#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        res = []
        rmin, cmin = 0, 0
        rmax, cmax = m-1,n-1
        while len(res) < m*n:
            r = rmin
            for c in range(cmin, cmax+1):
                res.append(matrix[r][c])
            if len(res) >= m*n:
                break
            rmin += 1
            c = cmax
            for r in range(rmin, rmax+1):
                res.append(matrix[r][c])
            if len(res) >= m*n:
                break
            cmax -= 1
            r = rmax
            for c in range(cmax, cmin-1, -1):
                res.append(matrix[r][c])
            if len(res) >= m*n:
                break
            rmax -= 1
            c = cmin
            for r in range(rmax, rmin-1, -1):
                res.append(matrix[r][c])
            cmin += 1
        return res
            

# @lc code=end

