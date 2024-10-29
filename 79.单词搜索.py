#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        visit = set()

        def dfs(r, c, idx):
            if idx>=len(word):
                return True
            if not (0<=r<m and 0<=c<n):
                return False
            if (r,c ) in visit:
                return False
            if board[r][c] != word[idx]:
                return False
            visit.add((r,c))
            for nr, nc in [[r,c-1],[r,c+1],[r-1,c],[r+1,c]]:
                if dfs(nr,nc, idx+1):
                    return True
            visit.remove((r,c))
            return False
        for r in range(m):
            for c in range(n):
                if dfs(r,c,0):
                    return True
        return False
# @lc code=end

