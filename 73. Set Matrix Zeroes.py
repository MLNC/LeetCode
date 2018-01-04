class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        zerosM = []
        zerosN = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    if i not in zerosM:
                        zerosM.append(i)
                    if j not in zerosN:
                        zerosN.append(j)
        for i in range(len(zerosM)):
            for j in range(n):
                matrix[zerosM[i]][j] = 0
        for j in range(len(zerosN)):
            for i in range(m):
                matrix[i][zerosN[j]] = 0
