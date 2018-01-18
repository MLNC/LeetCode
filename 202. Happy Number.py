class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        set = []
        while n!=1:
            curr = 0
            while n > 0:
                curr += (n%10) ** 2
                n = n// 10
            n = curr
            if n not in set:
                set.append(n)
            else:
                return False
        return True
