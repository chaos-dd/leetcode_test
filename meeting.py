#给定一系列的会议时间间隔，包括起始和结束时间[(s1,e1)，(s2,e2)，…(si < ei)，确定一个人是否可以参加所有会议。
#0≤intervals.length≤10 
#[(0,8), (8,10)] 在 8 这一时刻不冲突
#输入: intervals = [(0,30),(5,10),(15,20)]
#输出: false
#解释:
#(0,30), (5,10) 和 (0,30),(15,20) 这两对会议会冲突
from typing import (
    List,
)
from lintcode import (
    Interval,
)

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        # Write your code here
        intervals = sorted(intervals, key=lambda x:x.start)
        for i in range(len(intervals)):
            if i > 0 and intervals[i].start < intervals[i-1].end:
                return False
        return True
    