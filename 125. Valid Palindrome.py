import re

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = re.sub(r'\W+', '', s).upper()
        return s == s[::-1]


solution = Solution()
print(solution.isPalindrome('sadfsd sdaf slk fdsa,'))
