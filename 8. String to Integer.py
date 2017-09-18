# review Regex

import re
class Solution(object):
    def myAtoiLong(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        if not str:
            return 0
        num = 0
        sign = 1
        if str[0] in ['-', '+']:
            if str[0] == '-' and len(str) > 1:
                sign = -1
                str = str[1:]
            elif str[0] == '+' and len(str) > 1:
                sign = 1
                str = str[1:]
            else:
                return 0

        if str[0] in range(9):
            for i in range(1, len(str)):
                try:
                    num = num * 10 + int(str[i])
                except:
                    break
        num = sign * num
        if num > 2147483647:
            return 2147483647
        elif num < -2147483648:
            return -2147483648
        else:
            return num

    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        str = re.findall('(^[\+\-0]*\d+)\D*', str)

        try:
            result = int(''.join(str))
            if result > 2147483647 > 0:
                return 2147483647
            elif result < -2147483648 < 0:
                return -2147483648
            else:
                return result
        except:
            return 0

solution = Solution()
print(solution.myAtoi('165161565'))
