#
# @lc app=leetcode.cn id=417 lang=python3
#
# [417] 太平洋大西洋水流问题
#

# @lc code=start
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def dfs(visit, i, j):
            if (i, j) in visit:
                return
            visit.add((i, j))
            for r, c in [[-1,0], [1, 0], [0, -1], [0, 1]]:
                nr, nc = i+r,j+c
                if not (nr >= 0 and nr < len(heights) and nc >=0 and nc < len(heights[0])):
                    continue
                if heights[nr][nc] >= heights[i][j] and (nr, nc) not in visit:
                    dfs(visit, nr, nc)
        visit1 = set()
        visit2 = set()
        #for i in range(len(heights)):
        #    dfs(visit1, i, 0)
        #for i in range(len(heights[0])):
        #    dfs(visit1, 0, i)
        #for i in range(len(heights)):
        #    dfs(visit2, i, len(heights[0])-1)
        #for i in range(len(heights[0])):
        #    dfs(visit2, len(heights)-1, i)

        def search(ls):
            visit = set()
            for tu in ls:
                dfs(visit, tu[0], tu[1])
            return visit
        visit1 = search([(i, 0) for i in range(len(heights))] + [(0, i) for i in range(len(heights[0]))])
        visit2 = search([(i, len(heights)-1) for i in range(len(heights))] + [(len(heights)-1, i) for i in range(len(heights))])

        return list(visit1 & visit2)

# @lc code=end

