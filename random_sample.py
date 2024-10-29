import sys
from collections import defaultdict
import random
import numpy as np
import bisect


data = defaultdict(lambda :0)
elements = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
n=10000
for i in range(n):
    index = np.random.normal(loc=len(elements)/2)
    index = max(0, min(len(elements)-1, int(index)))
    data[elements[index]] += 1
         
for k, cnt in sorted(data.items()):
    print(k, cnt)

def sample(data, n):
    total = sum(data.values())
    cum_prob = []
    key = []
    cur = 0
    for k, cnt in data.items():
        cur += cnt
        key.append(k)
        cum_prob.append(cur)
    res = defaultdict(lambda :0)
    for i in range(n):
        rd = random.uniform(0, cum_prob[-1])
        index = bisect.bisect_left(cum_prob, rd)
        res[key[index]] += 1
    return res

res = sample(data, 10000)
print('='*100)
for k, cnt in sorted(res.items()):
    print(k, cnt)