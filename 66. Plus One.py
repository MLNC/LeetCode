# List/String/Array is somehow equal in Python

class Solution(object):
    def plusOneLong(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits[len(digits) - 1] += 1
        flag = False
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] >= 10:
                digits[i] = digits[i] % 10
                if i == 0:
                    flag = True
                else:
                    digits[i - 1] += 1
        if flag:
            digits.append(0)
            for i in range(len(digits) - 2, -1, -1):
                if i == 0:
                    digits[1] = digits[0]
                    digits[0] = 1
                else:
                    digits[i + 1] = digits[i]
        return digits

    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = 0
        for i in range(len(digits)):
            num = num * 10 + digits[i]
        return [int(i) for i in str(num + 1)]

    def plusOneReduce(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = reduce(lambda x, y: x * 10 + y, digits) +1
        return [int(i) for i in str(num)]
