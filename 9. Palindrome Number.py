# Palindrome 回文

class Solution(object):
    def isPalindromeString(self, x):
        """
        :type x: int
        :rtype: bool
        """
        y = x.__str__()
        return x[::-1] == x

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x % 10 == 0 and x > 0):
            return False
        rev = 0
        while x > rev:
            rev = rev * 10 + x % 10
            x = x / 10
            print(rev, x)
        return rev == x or x == rev / 10


solution = Solution()
print(solution.isPalindrome(1000021))
