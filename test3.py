import random
from typing import List
class Solution:

    def __init__(self, nums: List[int]):
        self.ori_data = nums[:]
        self.data = nums[:]
    def reset(self) -> List[int]:
        self.data = self.ori_data[:]
        return self.data
    def shuffle(self) -> List[int]:
        idx1 = random.randint(0, len(self.data)-1)
        idx2 = random.randint(0, len(self.data)-1)
        self.data[idx1], self.data[idx2] = self.data[idx2], self.data[idx1]
        return self.data
        # import random
        # for i in range(len(self.data)):
        #     pos = random.randint(i, len(self.data)-1)
        #     self.data[i], self.data[pos] = self.data[pos], self.data[i]
        # return self.data

ss = Solution([1,2,3,4,5,6,7,8,9])

dic = {}
for i in range(1, 10):
    dic[i] = [0]*9

for i in range(1000000):
    nums = ss.shuffle()
    for idx, n in enumerate(nums):
        dic[n][idx] += 1
for k, v in dic.items():
    print(k, v)
