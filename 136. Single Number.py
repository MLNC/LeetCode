class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        for i in nums:
            try:
                dict.pop(i)
            except:
                dict[i] = 1
        return dict.popitem()[0]

    def singleNumberMath(self, nums):
        return 2 * sum(set(nums)) - sum(nums)
