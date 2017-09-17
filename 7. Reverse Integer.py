# cmp(a,b) = (a>b) - (a<b)
# repr()
# [::-1]
# true is 1, false is 0


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = (x > 0) - (x < 0)
        r = int(repr(s * x)[::-1])
        return s * r * (r < 2 ** 31)


solution = Solution()
print(solution.reverse(1000))
