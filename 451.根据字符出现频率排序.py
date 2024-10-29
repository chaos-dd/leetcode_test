#
# @lc app=leetcode.cn id=451 lang=python3
#
# [451] 根据字符出现频率排序
#

# @lc code=start
class Solution:
    def frequencySort(self, s: str) -> str:
        def method1():
            dic = {}
            for c in s:
                if c not in dic:
                    dic[c] = 0
                dic[c] += 1
            res = []
            for c, cnt in sorted(dic.items(), key=lambda x:-x[1]):
                res.extend([c]*cnt)
            return ''.join(res)
        def method2():
            dic = {}
            max_cnt = 0
            for c in s:
                if c not in dic:
                    dic[c] = 0
                dic[c] += 1
                max_cnt = max(max_cnt, dic[c])
            bucket = [[] for _ in range(max_cnt+1)]
            for c, cnt in dic.items():
                bucket[cnt].append(c)
            res = []
            for cnt in reversed(range(len(bucket))):
                bu = bucket[cnt]
                for c in bu:
                    res.extend([c]*cnt)
            return ''.join(res)
        return method2()


# @lc code=end

