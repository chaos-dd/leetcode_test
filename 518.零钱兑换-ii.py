#
# @lc app=leetcode.cn id=518 lang=python3
#
# [518] 零钱兑换 II
#

# @lc code=start
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        def method1():
            from functools import cache
            @cache
            def count(i, amount):
                if amount<0 or i < 0:
                    return 0
                if amount == 0:
                    return 1
                return count(i-1, amount) + count(i, amount-coins[i])
            return count(len(coins)-1, amount)
                    

        def method2():
            n = len(coins)
            f = [[0] * (amount + 1) for _ in range(n + 1)]
            f[0][0] = 1
            for i, x in enumerate(coins):
                for c in range(amount + 1):
                    if c < x:
                        f[i + 1][c] = f[i][c]
                    else:
                        f[i + 1][c] = f[i][c] + f[i + 1][c - x]
            return f[n][amount]
        def method3():
            #每次用完每个coin后面不在使用了
            n = len(coins)
            f = [[0]*(n+1) for _ in range(amount + 1)]
            f[0][0] = 1
            for c in range(amount + 1):
                for i, x in enumerate(coins):
                    if c < x:
                        f[c][i + 1] = f[c][i]
                    else:
                        #这里f[c][i]，说明本次不用i+1个coin
                        #同时保证后面迭代也不会使用第i+1个coin
                        f[c][i + 1] = f[c][i] + f[c-x][i + 1]
            return f[amount][n]
        def method4():
            n = len(coins)
            f = [0] * (amount + 1)
            f[0] = 1
            #如果先循环amount, amount-coins[i]后，可能下次还会取到coins[i]，造成重复
            for i, x in enumerate(coins):
                for c in range(amount + 1):
                    if c >= x:
                        f[c] += f[c - x]
            return f[amount]
        def method5():
            #错误，选取顺序是无关的。如果是爬楼梯就是顺序有关的
            n = len(coins)
            f = [0] * (amount + 1)
            f[0] = 1
            #如果先循环amount, amount-coins[i]后，可能下次还会取到coins[i]，造成重复
            for c in range(amount + 1):
                #循环完一次之后，代表不在使用这个coin了，如果放在里面，后面还会遇到
                for i, x in enumerate(coins):
                    if c >= x:
                        f[c] += f[c - x]
            return f[amount]
        def method6():
            #错误
            n = len(coins)
            f = [0] *(n+1)
            f[0] = 1
            for c in range(amount + 1):
                for i, x in enumerate(coins):
                    if c < x:
                        f[c][i + 1] = f[c][i]
                    else:
                        #依赖前面c-x行，所以压缩不了
                        f[c][i + 1] = f[c][i] + f[c-x][i + 1]
            return f[amount][n]

        return method3()

# @lc code=end

