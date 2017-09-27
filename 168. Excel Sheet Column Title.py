class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = ''
        while n > 0:
            result = result + chr((n-1) % 26 + 65)
            n = (n-1) // 26
        return result[::-1]


solution = Solution()
print(solution.convertToTitle(993))