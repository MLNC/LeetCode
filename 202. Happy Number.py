class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        dict = set()
        n = str(n)
        while True:
            count = 0
            for i in n:
                count += int(i)*int(i)
            if count == 1:
                return True
            if count not in dict:
                dict.add(count)
                n = str(count)
            else:
                return False
