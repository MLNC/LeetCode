class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for i in tokens:
            if i.isdigit() or (i[0] == "-" and i[1:].isdigit()):
                stack.append(int(i))
            elif i == "+":
                b = stack.pop()
                a = stack.pop()
                stack.append(a + b)
            elif i == "-":
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)
            elif i == "*":
                b = stack.pop()
                a = stack.pop()
                stack.append(a * b)
            elif i == "/":
                b = stack.pop()
                a = stack.pop()
                if a * b < 0 and a % b != 0:
                    stack.append(a / b + 1)
                else:
                    stack.append(a / b)
        return stack.pop()

