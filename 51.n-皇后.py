#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#
#
# void backtracking(参数) {
#     if (终止条件) {
#         存放结果;
#         return;
#     }

#     for (选择：本层集合中元素（树中节点孩子的数量就是集合的大小）) {
#         处理节点;
#         backtracking(路径，选择列表); // 递归
#         回溯，撤销处理结果
#     }
# }

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:



# @lc code=end

