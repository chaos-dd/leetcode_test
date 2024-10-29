#
# @lc app=leetcode.cn id=304 lang=python3
#
# [304] 二维区域和检索 - 矩阵不可变
#

# @lc code=start
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rown = len(matrix)
        coln = len(matrix[0])
        self.pre_sum = [[0]*(coln+1) for _ in range(rown+1)]

        for r in range(1, rown+1):
            for c in range(1, coln+1):
                self.pre_sum[r][c] = self.pre_sum[r-1][c] \
                    +self.pre_sum[r][c-1] \
                    -self.pre_sum[r-1][c-1] \
                    + matrix[r-1][c-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = self.pre_sum[row2+1][col2+1] \
            - self.pre_sum[row1][col2+1] \
            - self.pre_sum[row2+1][col1] \
            + self.pre_sum[row1][col1]
        return ans



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
# @lc code=end

