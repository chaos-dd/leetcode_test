#
# @lc app=leetcode.cn id=932 lang=python3
#
# [932] 漂亮数组
#

# @lc code=start
class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        # 漂亮数组线性变换后还是漂亮数组
        # 两个漂亮数组合并在一起也是漂亮数组
        # 一半奇数，一半偶数，并且两个半部分也是飘飘数组，最后组合后一定是
        # 因为2*nk是偶数，ni+nj是奇数
        from functools import cache
        @cache
        def helper(n):
            if n == 1:
                return [1]
            return [2*x-1 for x in helper((n+1)//2)] + [2*x for x in helper(n//2)]
        return helper(n)
# @lc code=end

