#
# @lc app=leetcode.cn id=241 lang=python3
#
# [241] 为运算表达式设计优先级
#

# @lc code=start
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def method1():
            from functools import cache
            @cache
            def dfs(s, e):
                res = []
                for i in range(s, e):
                    if expression[i] == '-' or expression[i] == '+' \
                    or expression[i] == '*':
                        res1 = dfs(s, i-1)
                        res2 = dfs(i+1,e)
                        for v1 in res1:
                            for v2 in res2:
                                if expression[i]=='-':
                                    res.append(v1-v2)
                                elif expression[i] == '+':
                                    res.append(v1+v2)
                                else:
                                    res.append(v1*v2)
                #全是数字
                if len(res)==0:
                    res.append(int(expression[s:e+1]))
                return res
            return dfs(0, len(expression)-1)

        return method1()

# @lc code=end

