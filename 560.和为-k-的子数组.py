#
# @lc app=leetcode.cn id=560 lang=python3
#
# [560] 和为 K 的子数组
#

# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        prefix = defaultdict(int)
        prefix[0] = 1
        cur = 0
        ans = 0
        for v in nums:
            cur += v
            ans += prefix[cur-k]
            prefix[cur]+=1
        return ans


        
# @lc code=end

