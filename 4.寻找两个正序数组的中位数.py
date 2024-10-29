#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def method1():
            nums = sorted(nums1+nums2)
            n=len(nums)
            if n % 2 == 1:
                return nums[n//2]
            else:
                return (nums[n//2] + nums[n//2-1])/2
        def method2():
            nums = []
            m,n = len(nums1), len(nums2)
            i,j=0,0
            while i<m and j < n:
                if nums1[i]<nums2[j]:
                    nums.append(nums1[i])
                    i+=1
                else:
                    nums.append(nums2[j])
                    j+=1
            if i < m:
                nums.extend(nums1[i:])
            if j < n:
                nums.extend(nums2[j:])
            n=len(nums)
            if n % 2 == 1:
                return nums[n//2]
            else:
                return (nums[n//2] + nums[n//2-1])/2
        return method2()

            
# @lc code=end

