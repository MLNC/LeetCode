class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buyPrice = []
        sellPrice = []
        for i in range(0,len(prices)-1):
            difference = len(buyPrice)-len(sellPrice)
            if prices[i] < prices[i+1]:
                if difference == 0:
                    buyPrice.append(prices[i])
                else:
                    continue
            else:
                if difference == 0:
                    continue
                else:
                    sellPrice.append(prices[i])
        if len(buyPrice) > len(sellPrice):
            sellPrice.append(prices[len(prices)-1])
        elif len(buyPrice) < len(sellPrice):
            buyPrice.pop()
        max = 0
        for i in range(len(buyPrice)):
            max += sellPrice[i] - buyPrice[i]
        return max

    def maxProfitShort(self,prices):
        if not prices or len(prices) == 1:
            return 0
        result = 0
        for i in range(1, len(prices)):
            result += max(0, prices[i]- prices[i-1])
        return result