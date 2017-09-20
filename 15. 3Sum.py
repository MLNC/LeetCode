# Two pointers

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = list(set(nums))
        nums.sort()
        print(nums)
        result = []
        for i in range(0, len(nums) - 2):
            head, tail = i + 1, len(nums) - 1
            while head < tail:
                total = nums[i] + nums[head] + nums[tail]
                if total < 0:
                    head += 1
                elif total > 0:
                    tail -= 1
                elif total == 0:
                    if [nums[i], nums[head], nums[tail]] not in result:
                        result.append([nums[i], nums[head], nums[tail]])
                    head += 1
        return result


s = Solution()
print(s.threeSum([-1, 0, 1]))
