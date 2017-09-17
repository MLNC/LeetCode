class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dict = {'(': ')', '[': ']', '{': '}'}
        stack =[]
        for char in s:
            if char in dict.keys():
                stack.append(dict[char])
            elif char in dict.values():
                if stack ==[] or stack.pop() != char:
                    return False
        return True

    def isValidlong(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []
        for i in range(0, len(s)):
            if stack.__len__() == 0:
                prev = -1
            else:
                prev = stack[stack.__len__() - 1]
            if s[i] == '(':
                stack.append(1)
            elif s[i] == '[':
                stack.append(2)
            elif s[i] == '{':
                stack.append(3)
            elif s[i] == ')':
                if stack.pop() != 1:
                    return False
            elif s[i] == ']':
                if stack.pop() != 2:
                    return False
            elif s[i] == '}':
                if stack.pop() != 3:
                    return False

        if stack.__len__() == 0:
            return True
        else:
            return False


solution = Solution()
print(solution.isValid('()'))
