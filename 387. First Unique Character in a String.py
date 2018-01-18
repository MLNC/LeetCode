class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        letters = 'abcdefghijklmnopqrstuvwxyz'
        resutls = []
        for i in letters:
            if s.count(i) == 1:
                resutls.append(s.index(i))
        if len(resutls) != 0:
            return min(resutls)
        else:
            return -1
