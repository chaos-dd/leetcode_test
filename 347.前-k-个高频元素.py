#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        import heapq
        counter = Counter(nums)
        hp = []
        for val, cnt in counter.items():
            if len(hp)<k:
                heapq.heappush(hp, (cnt, val))
            else:
                if cnt > hp[0][0]:
                    heapq.heappop(hp)
                    heapq.heappush(hp, (cnt, val))
        return [x[1] for x in hp]
                
        
# @lc code=end

