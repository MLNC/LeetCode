# regex: \1 in the same pattern itself
# regex: \1* same pattern itself with several times



import re


class Solution(object):

    # **********DO NOT UNDERSTAND
    # **********Review REGEX

    # using a regular expression
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        for _ in range(n - 1):
            s = re.sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1), s)
        return s

    # using a regular expression
    def countAndSay1(self, n):
        s = '1'
        for _ in range(n - 1):
            s = ''.join(str(len(group)) + digit
                        for group, digit in re.findall(r'((.)\2*)', s))
        return s

    # using groupby()
    def countAndSay2(self, n):
        s = '1'
        for _ in range(n - 1):
            s = ''.join(str(len(list(group))) + digit
                        for digit, group in itertools.groupby(s))
        return s


solution = Solution()
print(solution.countAndSay(5))
