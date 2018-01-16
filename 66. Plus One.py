# List/String/Array is somehow equal in Python

class Solution(object):
    def plusOneLong(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 0
        length = len(digits)
        digits[length-1] += 1
        for i in range(length):
            digits[length-1-i] += carry
            if digits[length-1-i] >= 10:
                digits[length-1-i] = digits[length-1-i] % 10
                carry = 1
            else:
                carry = 0
        if carry == 1:
            digits = [1] + digits
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
