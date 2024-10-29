#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
#

# @lc code=start
class MinStack:

    def __init__(self):
        self.st = []
        self.st_min = []
        

    def push(self, val: int) -> None:
        self.st.append(val)
        if len(self.st_min) == 0 or val < self.st_min[-1]:
            self.st_min.append(val)
        else:
            self.st_min.append(self.st_min[-1])

    def pop(self) -> None:
        self.st_min.pop()
        return self.st.pop()

    def top(self) -> int:
        return self.st[-1]
        

    def getMin(self) -> int:
        return self.st_min[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

