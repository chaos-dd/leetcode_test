#
# @lc app=leetcode.cn id=278 lang=python3
#
# [278] 第一个错误的版本
#

# @lc code=start
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

# def isBadVersion(x):
#     return x >=1
class Solution:
    def firstBadVersion(self, n: int) -> int:

        def check(l, r):
            while l <= r:
                mid = (l+r)//2
                # print(l,r,mid)
                if isBadVersion(mid):
                    r = mid - 1
                else:
                    l = mid + 1
            return l
        return check(1, n)
            

# ss = Solution()
# print(ss.firstBadVersion(3))
        
# @lc code=end

