#
# @lc app=leetcode.cn id=785 lang=python3
#
# [785] 判断二分图
#

# @lc code=start
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def method1():
            if len(graph) == 0:
                return False
            n = len(graph)
            parent = [i for i in range(n+2)]
            def find(i):
                while parent[i] != i:
                    parent[i] = parent[parent[i]]
                    i = parent[i]
                return i
            def union(i,j):
                parent[find(i)] = find(j)
            for i in range(len(graph)):
                for j in graph[i]:
                    if find(i) == find(j):
                        return False
                    union(j, graph[i][0])
            return True
        def method2():
             
            n = len(graph)
            color = [0] * n
            def dfs(i, c):
                color[i] = c
                for j in graph[i]:
                    if color[j] == 0:
                        # color[j] = 1 if c == 2 else 2
                        if not dfs(j, 1 if c == 2 else 2):
                            return False
                    elif c == color[j]:
                        return False
                return True
            for i in range(n):
                if color[i] == 0:
                    if not dfs(i, 1):
                        return False
            return True
        return method2()
    
# @lc code=end

