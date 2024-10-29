#
# @lc app=leetcode.cn id=1870 lang=python3
#
# [1870] 准时到达的列车最小时速
#

# @lc code=start
class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if hour<len(dist)-1:
           return -1
        import math
        #l, r = 1,1e5/0.01
        l, r = 1,1e7
        def check(m):
           ans = 0
           for i in range(len(dist)-1):
               ans += math.ceil(max(1, dist[i]/m))
           ans += dist[-1]/m
           return ans <= hour

        ans = float('inf')
        while l <= r:
           m = (l+r)//2
           if check(m):
               ans = min(ans, m)
               r = m - 1
           else:
               l = m + 1
        return int(ans) if ans != float('inf') else -1
        
        # n = len(dist)
        # hr = round(hour * 100)
        # # 时间必须要大于路程段数减 1
        # if hr <= 100 * (n - 1):
        #     return -1
        # # 判断当前时速是否满足时限
        # def check(speed: int) -> bool:
        #     t = 0
        #     # 前 n-1 段中第 i 段贡献的时间： ceil(dist[i] / mid)
        #     for i in range(n - 1):
        #         t += (dist[i] - 1) // speed + 1
        #     # 最后一段贡献的时间： dist[n-1] / mid
        #     t *= speed
        #     t += dist[-1]
        #     return t * 100 <= hr * speed   # 通分以转化为整数比较
        
        # # 二分
        # l, r = 1, 10 ** 7
        # while l <= r:
        #     mid = l + (r - l) // 2
        #     if check(mid):
        #         r = mid - 1
        #     else:
        #         l = mid + 1
        # return l

# @lc code=end

