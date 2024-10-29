#
# @lc app=leetcode.cn id=452 lang=python3
#
# [452] 用最少数量的箭引爆气球
#

# @lc code=start
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda x:x[1])
        res = 0
        right = float('-inf')
        for i in range(len(points)):
            if points[i][0] > right:
                res += 1
                right = points[i][1]
            # print(i, right, res)
        return res

# @lc code=end

