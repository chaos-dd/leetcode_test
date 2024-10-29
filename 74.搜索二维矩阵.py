#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m*n-1
        while left <= right:
            mid = (left+right)//2
            r = mid//n
            c = mid%n
            if target==matrix[r][c]:
                return True
            elif target > matrix[r][c]:
                left = mid + 1
            else:
                right = mid -1
        return False
        
# @lc code=end

