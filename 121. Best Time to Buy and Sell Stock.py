import sys

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min = sys.maxsize
        maxProfit = 0
        for i in range(0, len(prices)):
            if prices[i] < min:
                min = prices[i]
            if prices[i] - min > maxProfit:
                maxProfit = prices[i] - min
        return maxProfit
