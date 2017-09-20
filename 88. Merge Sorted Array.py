# Thoughts:
# 1. put two arrays together, then quick sort. O(n log(n))
# 2. utilize python build-in function sort()
# 3. go one by one from the head of the list. best O(n+m), worst O(a log(a)) where a = max(n,m).
# 4. go one by one from the back. O(n+m)

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]
