import random

def weighted_random_sample(d):
    # 计算所有 value 的总和
    total = sum(d.values())
    
    # 生成一个 0 到 total 之间的随机数
    rand_val = random.uniform(0, total)
    
    # 遍历字典，确定随机数落在的区间
    cumulative_sum = 0
    for key, count in d.items():
        cumulative_sum += count
        if rand_val < cumulative_sum:
            return key

# 测试
char_counts = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
samples = [weighted_random_sample(char_counts) for _ in range(1000)]

# 统计每个字符出现的次数
from collections import Counter
counter = Counter(samples)

print("Sample counts:", counter)
