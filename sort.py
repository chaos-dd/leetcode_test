import time
import random

def quick_sort(arr):
    def _partition(arr, l, r):
        idx = random.randint(l, r)
        arr[idx], arr[l] = arr[l], arr[idx]
        key = arr[l]
        while l < r:
            while l < r and arr[r] >= key:
                r -= 1
            arr[l] = arr[r]
            while l < r and arr[l] <= key:
                l += 1
            arr[r] = arr[l]
        arr[r] = key
        return l
    
    def _qsort(arr, l, r):
        if l >= r:
            return
        pos = _partition(arr, l, r)
        _qsort(arr, l, pos - 1)
        _qsort(arr, pos + 1, r)
    _qsort(arr, 0, len(arr)-1)

    pass
    
def merge_sort(arr):

    def _merge(tmp, arr, s1, e1, s2, e2):
        i, j, k = s1, s2, s1
        while i <= e1 and j <= e2:
            if arr[i] < arr[j]:
                tmp[k] = arr[i]
                i += 1
            else:
                tmp[k] = arr[j]
                j += 1
            k += 1
        while i <= e1:
            tmp[k] = arr[i]
            i += 1
            k += 1
        while j <= e2:
            tmp[k] = arr[j]
            j += 1
            k += 1
        for i in range(s1, e2+1):
            arr[i] = tmp[i]
    def _merge_sort(tmp, arr, l, r):
        if l >= r:
            return
        mid = (l+r)//2
        _merge_sort(tmp, arr, l, mid)
        _merge_sort(tmp, arr, mid+1, r)
        _merge(tmp, arr, l, mid, mid+1, r)
    tmp=[0]*len(arr)
    _merge_sort(tmp, arr, 0, len(arr)-1)
    pass

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    pass

def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        key = arr[j]
        while j > 0 and arr[j-1]>key:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = key
    pass

def selection_sort(arr):
    for i in range(len(arr)):
        idx = i
        for j in range(i, len(arr)):
            if arr[j] < arr[idx]:
                idx = j
        arr[i], arr[idx] = arr[idx], arr[i]

    pass

def heap_sort(arr):

    def _heapify(arr, hps, root):
        while True:
            l = 2*root+1
            r = 2*root+2
            large = root
            while l < hps and arr[l] > arr[large]:
                large = l
            while r < hps and arr[r] > arr[large]:
                large = r
            if large != root:
                arr[root], arr[large] = arr[large], arr[root]
                root = large
            else:
                break
    for i in range(len(arr)//2-1, -1, -1):
        _heapify(arr, len(arr), i)
    hps = len(arr)
    while hps > 0:
        arr[0], arr[hps-1] = arr[hps-1], arr[0]
        hps -= 1
        _heapify(arr, hps, 0)

    pass

def heap_sort2(arr):
    def _sift_down(arr, hps, root):
        while True:
            l = 2*root+1
            r = 2*root+2
            large = root
            if l < hps and arr[l] > arr[large]:
                large = l
            if r < hps and arr[r] > arr[large]:
                large = r
            if large != root:
                arr[large], arr[root] = arr[root], arr[large]
                root = large
            else:
                break
    def _heapify(arr, hps):
        for i in reversed(range(hps//2)):
            _sift_down(arr, hps, i)
    _heapify(arr, len(arr))
    hps = len(arr)
    while hps > 0:
        arr[0], arr[hps-1] = arr[hps-1], arr[0]
        hps -= 1
        _sift_down(arr, hps, 0)
    
    pass

def counting_sort(arr):
    minv, maxv = min(arr), max(arr)
    count = [0] * (maxv - minv +1)
    for v in arr:
        count[v-minv] += 1
    index = 0
    for idx, cnt in enumerate(count):
        while cnt > 0:
            arr[index] = minv + idx
            index += 1
            cnt -= 1

def bucket_sort(arr):
    minv, maxv = min(arr), max(arr)
    bucket_num = 20
    bucket_range = (maxv - minv) // bucket_num
    bucket = [[] for _ in range(bucket_num)]
    for v in arr:
        idx = (v - minv)//bucket_range
        if idx == bucket_num:
            idx -= 1
        bucket[idx].append(v)

    output = []
    for nums in bucket:
        output.extend(sorted(nums))
    arr[:] = output[:]


# 验证排序算法是否正确
def is_correctly_sorted(arr, sorted_arr):
    return arr == sorted_arr

# 测试函数
def test_sorting_algorithms():
    algorithms = {
        "Bubble Sort": bubble_sort,
        "Selection Sort": selection_sort,
        "Insertion Sort": insertion_sort,
        "Quick Sort": lambda arr: quick_sort(arr),
        "Merge Sort": lambda arr: merge_sort(arr),
        "Heap Sort":heap_sort,
        "Heap Sort2":heap_sort2,
        "Counting Sort":counting_sort,
        "Bucket Sort":bucket_sort,
        #"Python's Built-in Sort": lambda arr: sorted(arr)
    }
    
    array_size = 1000
    test_array = [random.randint(0, array_size) for _ in range(array_size)]
    # print(test_array)
    # test_array = [5,4,3]
    correct_sorted_array = sorted(test_array)
    
    for name, func in algorithms.items():
        arr_copy = test_array.copy()
        start_time = time.time()
        func(arr_copy)
        sorted_array = arr_copy
        end_time = time.time()
        
        # 验证排序算法的正确性
        if is_correctly_sorted(sorted_array, correct_sorted_array):
            print(f"{name} is correct and took {end_time - start_time:.6f} seconds")
        else:
            print(f"{name} is incorrect")

# 运行测试
test_sorting_algorithms()


# quick_sort([4,3])