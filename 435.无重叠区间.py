#
# @lc app=leetcode.cn id=435 lang=python3
#
# [435] 无重叠区间
#

# @lc code=start
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x:x[1])
        l, r = 0, 1
        res = 0
        while r < len(intervals):
            if intervals[r][0] >= intervals[l][1]:
                #无交集
                l = r
                r += 1
            else:
                #有交集
                r += 1
                res += 1
        return res
# @lc code=end

