# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        median = len(nums) // 2
        root = TreeNode(nums[median])
        root.left = self.sortedArrayToBST(nums[:median])
        root.right = self.sortedArrayToBST(nums[median + 1:])
        return root
