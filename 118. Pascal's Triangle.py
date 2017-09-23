# review map

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        if numRows == 0:
            return result
        currentLevel = [1]
        result.append(currentLevel)
        for i in range(1, numRows):
            nextLevel = []
            nextLevel.append(currentLevel[0])
            for j in range(1, i):
                nextLevel.append(currentLevel[j - 1] + currentLevel[j])
            nextLevel.append(currentLevel[len(currentLevel) - 1])
            currentLevel = nextLevel
            result.append(nextLevel)
        return result

    def generateMap(self, numRows):
        res = [[1]]
        for i in range(1, numRows):
            res += [map(lambda x, y: x + y, res[-1] + [0], [0] + res[-1])]
        return res[:numRows]


solution = Solution()
print(solution.generate(5))
