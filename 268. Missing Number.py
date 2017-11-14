class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return len(nums)

    def missingNumberMath(self,nums):
        n = len(nums)
        return n * (n+1) / 2 - sum(nums)