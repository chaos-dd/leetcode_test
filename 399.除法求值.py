#
# @lc app=leetcode.cn id=399 lang=python3
#
# [399] 除法求值
#

# @lc code=start
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        from collections import defaultdict
        graph = defaultdict(list)
        for idx, (a, b) in enumerate(equations):
            graph[a].append((b, values[idx]))
            graph[b].append((a, 1.0/values[idx]))
        def dfs(start, end, path):
            if start not in graph or end not in graph:
                return -1.0
            if start == end:
                return 1.0
            res = -1.0
            path.add(start)
            for new_start, val in graph[start]:
                if new_start in path:
                    continue
                new_res = dfs(new_start, end, path)
                if new_res < 0:
                    continue
                res = val * new_res
                break
            path.remove(start)
            return res
        ans = []
        for a, b in queries:
            ans.append(dfs(a, b, set()))
        return ans
        
# @lc code=end

