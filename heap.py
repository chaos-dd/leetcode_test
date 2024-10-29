class MinHeap:
    def __init__(self):
        # 使用列表来存储堆元素
        self.heap = []

    def push(self, val):
        # 将新元素添加到堆的末尾
        self.heap.append(val)
        # 调整堆以保持最小堆性质
        self._sift_up(len(self.heap) - 1)

    def pop(self):
        if len(self.heap) == 0:
            return None  # 堆为空时返回None
        # 将堆顶元素与最后一个元素交换，然后移除堆顶元素
        self._swap(0, len(self.heap) - 1)
        min_val = self.heap.pop()
        # 调整堆以保持最小堆性质
        self._sift_down(0)
        return min_val

    def heapify(self, array):
        # 直接将数组变为堆
        self.heap = array
        # 从最后一个非叶子节点开始向上调整堆
        for i in reversed(range(len(self.heap) // 2)):
            self._sift_down(i)

    def _sift_up(self, idx):
        # 上浮操作
        parent_idx = (idx - 1) // 2  # 父节点的索引
        # 如果当前节点比其父节点小，交换它们的位置
        if idx > 0 and self.heap[idx] < self.heap[parent_idx]:
            self._swap(idx, parent_idx)
            # 递归调用，继续调整父节点的位置
            self._sift_up(parent_idx)

    def _sift_down(self, idx):
        # 下沉操作
        left_child_idx = 2 * idx + 1
        right_child_idx = 2 * idx + 2
        smallest_idx = idx

        # 找出左右孩子中较小的那个
        if left_child_idx < len(self.heap) and self.heap[left_child_idx] < self.heap[smallest_idx]:
            smallest_idx = left_child_idx
        if right_child_idx < len(self.heap) and self.heap[right_child_idx] < self.heap[smallest_idx]:
            smallest_idx = right_child_idx

        # 如果当前节点比其子节点大，交换它们的位置
        if smallest_idx != idx:
            self._swap(idx, smallest_idx)
            # 递归调用，继续调整子节点的位置
            self._sift_down(smallest_idx)

    def _swap(self, i, j):
        # 辅助方法：交换列表中的两个元素
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __str__(self):
        # 返回堆的字符串表示形式
        return str(self.heap)

import heapq
# 示例使用
heap = MinHeap()
heap.push(10)
heap.push(5)
heap.push(14)
heap.push(2)
heap.push(11)
print("Heap after push operations:", heap)
hp = []
heapq.heappush(hp, 10)
heapq.heappush(hp, 5)
heapq.heappush(hp, 14)
heapq.heappush(hp, 2)
heapq.heappush(hp, 11)
print('verfiy ', hp)

min_val = heap.pop()
print("Popped element:", min_val)
print("Heap after pop operation:", heap)
min_val2 = heapq.heappop(hp)
print('verify pop', min_val2)
print('verify after pop', hp)

array = [3, 9, 2, 1, 4, 5]
heap.heapify(array)
print("Heap after heapify operation:", heap)
array = [3, 9, 2, 1, 4, 5]
heapq.heapify(array)
print('verify heapify', array)