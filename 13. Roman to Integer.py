# Roman numeral 罗马数字

class Solution(object):
    def romanToInt(self, s):
        values = {
            "M": 1000, "D": 500,
            "C": 100, "L": 50,
            "X": 10, "V": 5,
            "I": 1
        }
        prev = 0
        total = 0
        for val in s:
            current = values[val]
            total += (current - 2 * prev) if (current > prev) else current
            prev = current
        return total

    def romanToIntRec(self, s):
        """
        :type s: str
        :rtype: int
        """
        return Solution.recurs(s)

    def recurs(s):
        """
        :type s:str
        :return: int
        """
        if s.__len__() == 1:
            if s.startswith('I'):
                return 1
            elif s.startswith('V'):
                return 5
            elif s.startswith('X'):
                return 10
            elif s.startswith('L'):
                return 50
            elif s.startswith('C'):
                return 100
            elif s.startswith('D'):
                return 500
            elif s.startswith('M'):
                return 1000
        elif s.startswith('I'):
            flag = 1
            if Solution.order.index(s[1]) > Solution.order.index(s[0]):
                flag = -1
            return 1 * flag + Solution.recurs(s[1:])
        elif s.startswith('V'):
            flag = 1
            if Solution.order.index(s[1]) > Solution.order.index(s[0]):
                flag = -1
            return 5 * flag + Solution.recurs(s[1:])
        elif s.startswith('X'):
            flag = 1
            if Solution.order.index(s[1]) > Solution.order.index(s[0]):
                flag = -1
            return 10 * flag + Solution.recurs(s[1:])
        elif s.startswith('L'):
            flag = 1
            if Solution.order.index(s[1]) > Solution.order.index(s[0]):
                flag = -1
            return 50 * flag + Solution.recurs(s[1:])
        elif s.startswith('C'):
            flag = 1
            if Solution.order.index(s[1]) > Solution.order.index(s[0]):
                flag = -1
            return 100 * flag + Solution.recurs(s[1:])
        elif s.startswith('D'):
            flag = 1
            if Solution.order.index(s[1]) > Solution.order.index(s[0]):
                flag = -1
            return 500 * flag + Solution.recurs(s[1:])
        elif s.startswith('M'):
            flag = 1
            if Solution.order.index(s[1]) > Solution.order.index(s[0]):
                flag = -1
            return 1000 * flag + Solution.recurs(s[1:])


solution = Solution()
print(solution.romanToInt('MMMCD'))
