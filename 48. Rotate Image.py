class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix) - 1
        for i in range((n + 2) // 2):
            a = 0
            if n % 2 == 0:
                a = i
            for j in range(a, (n + 2) // 2):
                # 0,1 to 1,3 ==> i,j to j,n-i
                # 1,3 to 3,2 ==> j,n-i to n-i,n-j
                # 3,2 to 2,0 ==> n-i,n-j to n-j,i
                # 2,0 to 0,1 ==> n-j,i to i,j
                tmp = matrix[i][j]
                print(i, j)
                matrix[i][j] = matrix[n - j][i]
                matrix[n - j][i] = matrix[n - i][n - j]
                matrix[n - i][n - j] = matrix[j][n - i]
                matrix[j][n - i] = tmp
        return

    def rotateShort(self, matrix):
        matrix[:] = zip(*matrix[::-1])


solution = Solution()
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
solution.rotate(a)
print(a)
