#
# @lc app=leetcode.cn id=769 lang=python3
#
# [769] 最多能完成排序的块
#

# @lc code=start
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        ans = 0
        mv = 0
        for i in range(len(arr)):
            mv = max(arr[i], mv)
            if mv == i:
                ans += 1
        return ans


# @lc code=end

