#
# @lc app=leetcode.cn id=684 lang=python3
#
# [684] 冗余连接
#

# @lc code=start
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def method1():
            n = len(edges)
            parent = [i for i in range(n+1)]
            def find(p):
                while parent[p] != p:
                    parent[p]=parent[parent[p]] #路径压缩
                    p = parent[p]
                return p
            def union(p, q):
                parent[find(p)] = find(q)
            
            for e in edges:
                if find(e[0]) == find(e[1]):
                    return e
                else:
                    union(e[0], e[1])
            return [-1,-1]
        def method2():
            n = len(edges)
            parent = [i for i in range(n+1)]
            size = parent[:]
            def find(p):
                while parent[p] != p:
                    parent[p] = parent[parent[p]]
                    p = parent[p]
                return p
            def union(i, j):
                pi, pj = find(i), find(j)
                if pi != pj:
                    if size[pi] < size[pj]:
                        size[pj] += size[pi]
                        parent[pi] = pj
                    else:
                        size[pi] += size[pj]
                        parent[pj] = pi
            for e in edges:
                if find(e[0]) == find(e[1]):
                    return e
                else:
                    union(e[0], e[1])
            return [-1, -1]
                
        return method2()

# @lc code=end

