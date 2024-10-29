#
# @lc app=leetcode.cn id=547 lang=python3
#
# [547] 省份数量
#

# @lc code=start
from collections import deque
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        def method1():
            def dfs(visit, i):
                visit[i] = 1
                for j in range(len(isConnected)):
                    if isConnected[i][j] == 1 and visit[j] == 0:
                        dfs(visit, j)
            
            visit = [0] * len(isConnected)
            res = 0
            for i in range(len(isConnected)):
                if visit[i] == 1:
                    continue
                dfs(visit, i)
                res += 1
            return res
    
        def method2():
            from collections import deque
            
            visit = set()
            res = 0
            for i in range(len(isConnected)):
                if i in visit:
                    continue
                dq = deque([i])
                while len(dq) > 0:
                    j = dq.popleft()
                    if j in visit:
                        continue
                    visit.add(j)
                    for k in range(len(isConnected)):
                        if k not in visit and isConnected[j][k] == 1:
                            dq.append(k)
                res += 1
            return res
                    
        def method3():

            parent = [i for i in range(len(isConnected))]

            def find(i):
                while parent[i] != i:
                    parent[i] = parent[parent[i]]
                    i = parent[i]
                return i
            def union(i, j):
                parent[find(i)] = find(j)
            
            for i in range(len(isConnected)):
                for j in range(i+1, len(isConnected)):
                    if isConnected[i][j] == 1:
                        union(i,j)
            res = 0
            for i in range(len(isConnected)):
                if parent[i] == i:
                    res += 1
            return res
        
        return method1()


# @lc code=end

