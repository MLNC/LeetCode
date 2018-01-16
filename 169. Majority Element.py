class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        set = {}
        for i in nums:
            if i not in set:
                set[i] = 1
            else:
                set[i] += 1
            if set[i] > len(nums)/2:
                return i
    def majorityElementSort(self,nums):
        nums = sorted(nums)
        return nums[len(nums) //2]