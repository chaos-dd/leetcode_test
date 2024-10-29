#
# @lc app=leetcode.cn id=912 lang=python3
#
# [912] 排序数组
#

# @lc code=start
import random
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def qsort(nums):
            def partition(nums, left, right):
                idx = random.randint(left, right)
                nums[left], nums[idx] = nums[idx], nums[left]
                key = nums[left]
                while left < right:
                    while left < right and nums[right] >= key:
                        right -= 1
                    nums[left] = nums[right]
                    while left < right and nums[left] <= key:
                        left += 1
                    nums[right] = nums[left]
                nums[left] = key
                return left
            
            def qsort(nums, left, right):
                if left >= right:
                    return
                mid = partition(nums, left, right)
                qsort(nums, left, mid - 1)
                qsort(nums, mid + 1, right)
            qsort(nums, 0, len(nums)-1)
        def merge_sort(nums):
            def merge(nums, l, r, tmp):
                if l >= r:
                    return
                mid = (l + r) // 2
                merge(nums, l, mid, tmp)
                merge(nums, mid + 1, r, tmp)
                s3 = l
                s1, s2 = l, mid + 1
                while s1 <= mid and s2 <= r:
                    if nums[s1] < nums[s2]:
                        tmp[s3] = nums[s1]
                        s1 += 1
                    else:
                        tmp[s3] = nums[s2]
                        s2 += 1
                    s3 += 1
                    
                while s1 <= mid:
                    tmp[s3] = nums[s1]
                    s3 += 1
                    s1 += 1
                while s2 <= r:
                    tmp[s3] = nums[s2]
                    s3 += 1
                    s2 += 1
                for i in range(l, r + 1):
                    nums[i] = tmp[i]
            tmp = [0] * len(nums)
            merge(nums, 0, len(nums) - 1, tmp)
        #merge_sort(nums)
        def bubble_sort(nums):
            for i in range(len(nums)):
                is_swap = False
                for j in range(len(nums) - i - 1):
                    if nums[j] > nums[j+1]:
                        nums[j], nums[j+1] = nums[j+1], nums[j]
                        is_swap = True
                if not is_swap:
                    break
        #bubble_sort(nums)
        def select_sort(nums):
            for i in range(len(nums)):
                min_idx = i
                for j in range(i + 1, len(nums)):
                    if nums[j] < nums[min_idx]:
                        min_idx = j
                nums[i], nums[min_idx] = nums[min_idx], nums[i]
        #select_sort(nums)
        def insert_sort(nums):
            for i in range(1, len(nums)):
                j = i - 1
                key = nums[i]
                while j >= 0 and nums[j] > key:
                    nums[j + 1] = nums[j]
                    j -= 1
                nums[j + 1] = key
        #insert_sort(nums)
        def heap_sort(nums):
            def heapify(nums, hps, r):
                l = 2 * r + 1
                while l < hps:
                    if l + 1 < hps and nums[l+1] > nums[l]:
                        l += 1
                    if nums[l] > nums[r]:
                        nums[r], nums[l] = nums[l], nums[r]
                        #交换后这个子树可能不满足最大堆了
                        r = l
                        l = 2 * r + 1
                    else:
                        break
                    
            for i in range(len(nums)//2 - 1, -1, -1):
                heapify(nums, len(nums), i)
            # print(nums)
            hps = len(nums)
            while hps > 0:
                nums[0], nums[hps-1] = nums[hps-1], nums[0]
                hps -= 1
                heapify(nums, hps, 0)
                # print(nums)
        heap_sort(nums)
        
        return nums
                

# @lc code=end

