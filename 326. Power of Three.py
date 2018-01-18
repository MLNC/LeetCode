class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and 1162261467 % n == 0

    def isPowerOfThreeStandard(self, n):
        if n <= 0:
            return False

        while n % 3 == 0:
            n = n / 3

        return True if n == 1 else False
