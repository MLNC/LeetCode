class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(nums[len(nums) - 1] + self.rob(nums[:-2]), self.rob(nums[:-1]))

    def robIterative(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        ans1 = nums[0]
        ans2 = 0
        ans = 0
        for i in range(1,len(nums)):
            ans = max(ans1, ans2 + nums[i])
            ans2 = ans1
            ans1 = ans
        return ans