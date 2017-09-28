class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            dic = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
            for j in range(9):
                n = board[i][j]
                if n != '.':
                    try:
                        dic.remove(n)
                    except:
                        print(1)
                        return False

        for j in range(9):
            dic = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
            for i in range(9):
                n = board[i][j]
                if n != '.':
                    try:
                        dic.remove(n)
                    except:
                        print(2)
                        return False

        for n in range(3):
            for m in range(3):
                dic = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
                for i in range(3):
                    for j in range(3):
                        n = board[3*n+i][3*m+j]
                        if n != '.':
                            try:
                                dic.remove(n)
                            except:
                                print(3)
                                return False

        return True


solution = Solution()
print(solution.isValidSudoku(
    '[".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]'))
