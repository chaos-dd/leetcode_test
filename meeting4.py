#给定一系列会议的开始时间、结束时间[[s1,e1]，[s2,e2]，…(si < ei)及他们的价值。你在同一时刻只能参加一个会议，请问你可以获得的最大价值是多少？

from typing import (
    List,
)
from collections import defaultdict
class Solution:
    """
    @param meeting: the meetings
    @param value: the value
    @return: calculate the max value
    """
    def max_value(self, meeting: List[List[int]], value: List[int]) -> int:
        # write your code here
        max_time = 0
        dic = defaultdict(list)
        for i in range(len(meeting)):
            max_time = max(max_time, meeting[i][1])
            dic[meeting[i][1]].append((meeting[i][0], value[i]))

        dp = [0] * (max_time + 1)
        for i in range(1, max_time + 1):
            dp[i] = dp[i - 1]
            for j in range(len(dic[i])):
                start = dic[i][j][0]
                value = dic[i][j][1]
                dp[i] = max(dp[i], dp[start] + value)
        return max(dp)
    def max_value2(self, meeting: List[List[int]], value: List[int]) -> int:
        # write your code here
        import heapq
        q = []
        cur, ans = 0, 0
        for start,end,val in sorted([[e[0], e[1], x] for e, x in zip(meeting, value)]):
            while len(q) != 0 and q[0][0]<=start:
                cur = max(cur, heapq.heappop(q)[1])
            ans = max(ans, cur+val)
            heapq.heappush(q, [end, cur+val])
        return ans