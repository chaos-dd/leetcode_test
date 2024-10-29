#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals=sorted(intervals, key=lambda x:x[0])
        left, right = intervals[0]
        ans = []
        for i in range(1, len(intervals)):
            if intervals[i][0] > right:
                ans.append((left, right))
                left, right = intervals[i]
            else:
                right = max(right, intervals[i][1])
        ans.append((left, right))
        return ans
# @lc code=end

