import time
import random

def quick_sort(arr):

    pass
    
def merge_sort(arr):

    pass

def bubble_sort(arr):

    pass

def insertion_sort(arr):

    pass

def selection_sort(arr):

    pass

def heap_sort(arr):

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
    

def counting_sort(arr):


def bucket_sort(arr):

    pass


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
    # test_array = [random.randint(10, 100) for _ in range(100)]
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