# logarithmic 对数的

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        while n >= 5:
            result += n//5
            n = n//5
        return result

solution = Solution()
print(solution.trailingZeroes(26))