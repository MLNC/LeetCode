class Solution(object):
    def removeDuplicates(self, A):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not A:
            return 0

        newTail = 0

        for i in range(1, len(A)):
            if A[i] != A[newTail]:
                newTail += 1
                A[newTail] = A[i]

        return newTail + 1

solution = Solution()
print(solution.removeDuplicates(list(range(0,100)).append(list(range(0,100)))))
