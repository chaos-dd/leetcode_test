#
# @lc app=leetcode.cn id=207 lang=python3
#
# [207] 课程表
#

# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict, deque
        graph = defaultdict(list)
        indeg = defaultdict(int)
        for a, b in prerequisites:
            graph[b].append(a)
            indeg[a]+=1
        dq = []
        for i in range(numCourses):
            if indeg[i] ==0:
                dq.append(i)
        while dq:
            n = dq.pop()
            for n2 in graph[n]:
                indeg[n2]-=1
                if indeg[n2]==0:
                    dq.append(n2)
        for i in range(numCourses):
            if indeg[i] != 0:
                return False
        return True
# @lc code=end

