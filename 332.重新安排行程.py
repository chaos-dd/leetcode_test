#
# @lc app=leetcode.cn id=332 lang=python3
#
# [332] 重新安排行程
#

# @lc code=start
from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        dic = defaultdict(lambda :[])
        for ti in tickets:
            dic[ti[0]].append(ti[1])
        ans = []
        for fr in dic:
            dic[fr].sort()

        def dfs(ans, mem):
            ans.append(fro)
            for to in dic[fro]:
                dfs(ans, to)
        dfs(ans, 'JFK')
        return ans


# @lc code=end

