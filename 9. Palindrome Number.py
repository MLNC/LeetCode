# Palindrome 回文

class Solution(object):
    def isPalindromeExtraSpace(self, x):
        """
        :type x: int
        :rtype: bool
        """
        y = x.__str__()
        if x[::-1] == x:
            return True
        else:
            return False

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        power = 1
        while x > power * 10:
            power *= 10

        while x >= 10:
            head = x / power
            tail = x % 10
            print(head, tail, x, power)
            if int(head) != int(tail):
                return False
            x = x % power
            power = power / 10
            if 0 < x/power < 1:
                return False
            x = x/10
            power = power/10
        return True


solution = Solution()
print(solution.isPalindrome(1000021))
