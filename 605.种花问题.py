#
# @lc app=leetcode.cn id=605 lang=python3
#
# [605] 种花问题
#

# @lc code=start
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        def method1():
            res = 0
            i = 0
            while i < len(flowerbed) and res < n:
                if flowerbed[i] == 0 and \
                (i == 0 or flowerbed[i-1] == 0) and \
                (i == len(flowerbed) - 1 or flowerbed[i+1] == 0):
                    res += 1
                    i += 2
                else:
                    i += 1
            return res == n
        def method2():
            res = 0
            for i in range(len(flowerbed)):
                if flowerbed[i] == 1:
                    continue
                if i > 0 and flowerbed[i-1] == 1:
                    continue
                if i < len(flowerbed) -1 and flowerbed[i+1] == 1:
                    continue
                flowerbed[i] = 1
                res += 1
                if res >= n:
                    break
            return n == 0 or res == n
        return method1()

# @lc code=end

