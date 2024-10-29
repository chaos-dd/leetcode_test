#
# @lc app=leetcode.cn id=621 lang=python3
#
# [621] 任务调度器
#

# @lc code=start
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        from collections import Counter, deque
        import heapq
        cnt = Counter(tasks)
        hp = [-c for c in cnt.values()]
        heapq.heapify(hp)
        dq = deque()
        time = 0
        while hp or dq:
            time += 1
            if hp:
                cur = heapq.heappop(hp)
                cur += 1
                if cur != 0:
                    dq.append((cur, time+n))
            if dq and dq[0][1] == time:
                heapq.heappush(hp, dq.popleft()[0])
        return time


        
# @lc code=end

