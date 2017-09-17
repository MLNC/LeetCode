class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0, len(nums)):
            if (target - nums[i]) in nums and i is not nums.index(target - nums[i]):
                return [i, nums.index(target - nums[i])]

    def twoSumBruteForce(self, nums, target):
        # O(n^2) time, O(1) space
        # time limit exceeded
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                print(i, j)
                if nums[i] + nums[j] == target:
                    return [i, j]


solution = Solution()
print(solution.twoSum([3, 2, 4], 6))
