#
# @lc app=leetcode.cn id=455 lang=python3
#
# [455] 分发饼干
#

# @lc code=start
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i, j = 0, 0
        res = 0
        while i < len(g) and j < len(s):
            if s[j]>=g[i]:
                i += 1
                j += 1
                res += 1
            else:
                j += 1

        return res


# @lc code=end

