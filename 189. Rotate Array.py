class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # String Manipulation

        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]

        # k times shift, reverse
        """
        nums[:] = nums[::-1]
        for i in range(k):
            nums.append(nums[0])
            nums.pop(0)
        nums[:] = nums[::-1]
        """

        # k times shift, brute force
