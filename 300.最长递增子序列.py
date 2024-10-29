#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长递增子序列
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def method1():
            n = len(nums)
            dp = [1]*n
            for i in range(1, n):
                j = i - 1
                while j >= 0:
                    if nums[i]>nums[j]:
                        dp[i] = max(dp[i], dp[j]+1)
                    j -= 1
            return max(dp)
        def method2():
            import bisect
            seq = []
            for x in nums:
                idx = bisect.bisect_left(seq, x)
                if idx >= len(seq):
                    seq.append(x)
                else:
                    seq[idx] = x
            return len(seq)
        return method2()
        
# @lc code=end

