# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        curr = root
        stack = []
        prev = - sys.maxsize - 1
        while curr or len(stack) != 0:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            if curr.val <= prev:
                return False
            else:
                prev = curr.val
            curr = curr.left

        return True
