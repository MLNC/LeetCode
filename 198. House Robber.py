class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        f(0) = nums[0]
        f(1) = max(num[0], num[1])
        f(k+1) = max( f(k-1) + nums[k+1], f(k) )
        '''
        last, now = 0, 0

        for num in nums:
            last, now = now, max(last + num, now)

        return now
