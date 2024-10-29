#
# @lc app=leetcode.cn id=470 lang=python3
#
# [470] 用 Rand7() 实现 Rand10()
#

# @lc code=start
# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        # 模拟 7 进制好理解些，把 rand7() 的值减 1 ，就成了 [0, 6]，
        # 模拟两位的 7 进制数，取 [0, 39] 范围内的值，对 10 取余后加一
        while True:
            x = (rand7()-1) * 7 + rand7() -1
            if x < 40:
                break
        return x % 10 + 1
    
        
# @lc code=end

