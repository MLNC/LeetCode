class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        for i in range(32):
            count += n & 1
            n = n >> 1
        return count

    def hammingWeightShort(self, n):
        return bin(n).count("1")
