# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        self.inorderHelper(root, result)
        return result


    def inorderHelper(self, root, result):
        if not root:
            return
        self.inorderHelper(root.left, result)
        result.append(root.val)
        self.inorderHelper(root.right, result)

    def inorderTraversalIterate(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        stack = []
        curr = root
        while curr or stack.__len__()!=0:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            result.append(curr.val)
            curr = curr.right

        return result