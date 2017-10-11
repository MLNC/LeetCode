class Solution(object):
    def countPrimes(self, n):  # TLE
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1:
            return 0
        s = set(range(2, n))
        for i in range(2, int(n / 2 + 1)):
            if i in s:
                multi = 2 * i
                while multi < n:
                    if multi in s:
                        s.remove(multi)
                    multi += i
        print(s)
        return (len(s))

    def countPrimesFast(self, n):
        if n < 3:
            return 0
        s = [True] * n
        s[0] = s[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if s[i]:
                for j in range(2, (n - 1) // i + 1):
                    s[i * j] = False
        return sum(s)


solution = Solution()
print(solution.countPrimes(499))
