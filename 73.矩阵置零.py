#
# @lc app=leetcode.cn id=73 lang=python3
#
# [73] 矩阵置零
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m,n=len(matrix),len(matrix[0])
        row_flag = [0]*n
        col_flag = [0]*m
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    row_flag[c] = 1
                    col_flag[r] = 1
        for r in range(m):
            for c in range(n):
                if row_flag[c] == 1:
                    matrix[r][c]=0
                if col_flag[r] == 1:
                    matrix[r][c]=0
                    
        
# @lc code=end

