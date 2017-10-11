class Solution(object):
    def maxSubArray(self, n):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not n:
            return 0

        curSum = maxSum = n[0]
        for num in n[1:]:
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)

        return maxSum
