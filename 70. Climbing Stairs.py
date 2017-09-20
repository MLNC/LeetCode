# 1 2 3 4 5 6
# 1 2 3 5 8 13
# like Fibonacci Number

import math

class Solution(object):
    def climbStairs(self, n):  # O(n)
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        l = list()
        l.append(1)
        l.append(2)
        if n <= 2:
            return l[n - 1]
        for i in range(2, n):
            l.append(l[i - 1] + l[i - 2])
        return l[n - 1]

    def climbStairsFibonacci(self, n):  # ** is O(log(n))
        return int(1 / math.sqrt(5) * (((1 + math.sqrt(5)) / 2) ** (n + 1) - ((1 - math.sqrt(5)) / 2) ** (n + 1)))
