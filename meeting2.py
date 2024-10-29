from typing import (
    List,
)
from lintcode import (
    Interval,
)

import heapq
def method1():
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        # Write your code here
        intervals = sorted(intervals, key=lambda x:x.start)
        hp = []
        for i in range(len(intervals)):
            #只弹出最近开完的一个
            if len(hp) != 0 and intervals[i].start>=hp[0]:
                heapq.heappop(hp)
            heapq.heappush(hp, intervals[i].end)
        return len(hp)

def method2():
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
    # Write your code here
        intervals = sorted(intervals, key=lambda x:x.start)

        hp = []
        res = 0
        for i in range(len(intervals)):
            if len(hp) != 0 and intervals[i].start>=hp[0]:
                heapq.heappop(hp)
            heapq.heappush(hp, intervals[i].end)
            res = max(res, len(hp))
        return res
def method3():
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
    # Write your code here
        intervals = sorted(intervals, key=lambda x:x.start)
        hp = []
        res = 0
        for i in range(len(intervals)):
            #已经开完的全部弹出
            while len(hp) != 0 and intervals[i].start>=hp[0]:
                heapq.heappop(hp)
            heapq.heappush(hp, intervals[i].end)
            #需要记录最大
            res = max(res, len(hp))
        return res

def method():
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        # Write your code here
        room = []
        for inte in intervals:
            room.append((inte.start, 1))
            room.append((inte.end, -1))
        room = sorted(room)
        res = 0
        num = 0
        for t, c in room:
            num += c
            res = max(res, num)
        return res