# Review Reduce, Map
import functools

class Solution(object):
    def letterCombinationsReduce(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        kvmaps = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        return functools.reduce(lambda acc, digit: [x + y for x in acc for y in kvmaps[digit]], digits, [''])
