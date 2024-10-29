#
# @lc app=leetcode.cn id=135 lang=python3
#
# [135] 分发糖果
#

# @lc code=start
class Solution:
    def candy(self, ratings: List[int]) -> int:
        def method1():
            n = len(ratings)
            nums = [1] * n
            #左规则
            for i in range(1, n):
                if ratings[i] > ratings[i-1]:
                    nums[i] = nums[i-1]+1
            #右规则
            for i in range(n-2, -1, -1):
                if ratings[i] > ratings[i+1]:
                    nums[i] = max(nums[i], nums[i+1] + 1)
            return sum(nums)
        def method2():
            data = [(ratings[idx], idx) for idx in range(len(ratings))]
            data = sorted(data, key=lambda x:x[0])

            from collections import defaultdict
            vals = defaultdict(lambda :0)

            for rating, idx in data:
                if idx > 0 and rating > ratings[idx-1]:
                    vals[idx] = vals[idx-1] + 1
                if idx < len(ratings) - 1 and rating > ratings[idx+1]:
                    vals[idx] = max(vals[idx], vals[idx+1]+1)
                vals[idx] = max(vals[idx], 1)
            return sum(vals.values())

        def method3():
            inc, dec, res = 1, 0, 1
            pre = 1
            for i in range(1, len(ratings)):
                if ratings[i] >= ratings[i-1]:
                    dec = 0
                    pre = 1 if ratings[i] == ratings[-1] else pre + 1
                    inc += 1
                    res += pre
                else:
                    pre = 1
                    dec += 1
                    res += dec
            return res

        return method3()

# @lc code=end

