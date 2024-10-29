#
# @lc app=leetcode.cn id=763 lang=python3
#
# [763] 划分字母区间
#

# @lc code=start
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        def method1():
            m = {}
            for c in s:
                if c not in m:
                    m[c] = 0
                m[c] += 1
            m2 = set()
            res = []
            l = 0
            for c in s:
                # print(c)
                l += 1
                m[c] -= 1
                m2.add(c)
                if m[c] == 0 and len(m2) == 1:
                    res.append(l)
                    l = 0
                    m2 = set()
                elif m[c] == 0:
                    m2.remove(c)
            return res
        def method2():
            m={}
            for idx, c in enumerate(s):
                m[c] = idx
            res = []
            l = 0
            end = 0
            for idx, c in enumerate(s):
                l += 1
                #结束位置最少是当前字母最右侧的下标
                end = max(end, m[c])
                if idx == end:
                    res.append(l)
                    l = 0
                    end = 0
            return res
        return method2()

# @lc code=end

