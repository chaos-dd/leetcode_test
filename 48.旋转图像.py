#
# @lc app=leetcode.cn id=48 lang=python3
#
# [48] 旋转图像
#

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def method1():
            m,n = len(matrix),len(matrix[0])
            for r in range(m//2):
                for c in range(n):
                    matrix[r][c], matrix[n-r-1][c]=matrix[n-r-1][c],matrix[r][c]
            for r in range(m):
                for c in range(r, n):
                    matrix[r][c], matrix[c][r]=matrix[c][r],matrix[r][c]
        
        def method2():
            m,n = len(matrix),len(matrix[0])
            for r in range(m//2):
                for c in range((n+1)//2):
                    tmp = matrix[r][c]
                    matrix[r][c] = matrix[n-c-1][r]
                    matrix[n-c-1][r] = matrix[n-r-1][n-c-1]
                    matrix[n-r-1][n-c-1] = matrix[c][n-r-1]
                    matrix[c][n-r-1]=tmp

        return method2()
            

# @lc code=end

