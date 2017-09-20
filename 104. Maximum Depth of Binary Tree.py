# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepthDFS(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        thislevel = [root]
        level = 0
        while thislevel:
            nextlevel = list()
            for n in thislevel:
                if n.left: nextlevel.append(n.left)
                if n.right: nextlevel.append(n.right)
            level += 1
            thislevel = nextlevel
        return level

    def maxDepthRecurrsively(self, root):
        if not root:
            return 0
        return 1+max(self.maxDepthRecurrsively(root.left), self.maxDepthRecurrsively(root.right))

