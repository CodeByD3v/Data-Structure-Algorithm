"""
4. Median of Two Sorted Arrays
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 
Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
"""
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        copy = []
        n = len(nums1)
        m = len(nums2)
        middle = 0
        i , j  = 0 , 0 
        while i < n and j < m:
            if nums1[i] < nums2[j]:
                copy.append(nums1[i])
                i+=1
              
            else:
                copy.append(nums2[j])
                j+=1
 
    
        if i == n:
            while j < m:
                copy.append(nums2[j])
                j += 1

       
        if j == m:
            while i < n:
                copy.append(nums1[i])
                i += 1
            
        if len(copy) % 2 != 0:
            middle = copy[len(copy)//2]
        
        else:
            left = copy[(len(copy) // 2) - 1]
            right = copy[len(copy)//2]
            middle = (left+right) / 2.0

        return middle

