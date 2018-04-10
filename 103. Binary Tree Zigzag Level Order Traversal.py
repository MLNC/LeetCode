# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        result = []
        level = [root]
        flag = True
        while level:
            temp = []
            tempresult = []
            for node in level:
                tempresult.append(node.val)
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            level = temp
            if flag:
                result.append(tempresult)
            else:
                result.append(tempresult[::-1])
            flag = - flag
        return result