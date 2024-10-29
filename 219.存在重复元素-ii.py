#
# @lc app=leetcode.cn id=219 lang=python3
#
# [219] 存在重复元素 II
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        def method1():
            from collections import defaultdict
            dic = defaultdict(list)
            for i, v in enumerate(nums):
                dic[v].append(i)
            for v, ls in dic.items():
                if len(ls) <= 1:
                    continue
                for i in range(len(ls)):
                    for j in range(i+1, len(ls)):
                        if abs(ls[i]-ls[j]) <= k:
                            return True
            return False
        def method2():
            from collections import defaultdict
            dic = dict()
            for i, v in enumerate(nums):
                if v in dic and i-dic[v] <= k:
                    return True
                dic[v] = i
            return False
        def method3():
            mem = set()
            for i, v in enumerate(nums):
                if i - k > 0:
                    mem.remove(nums[i-k-1])
                if v in mem:
                    return True
                mem.add(v)
            return False
        return method3()

# @lc code=end

