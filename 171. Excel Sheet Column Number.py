class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        result = 0
        for i in s:
            print(i)
            result = result * 26 + ord(i) - 64
        return result


solution = Solution()
print(solution.titleToNumber('AA'))
