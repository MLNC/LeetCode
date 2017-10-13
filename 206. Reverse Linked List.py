# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        l = []
        while head:
            l.append(head)
            head = head.next
            l[len(l)-1].next = None
        result = l.pop()
        head = result
        while l:
            head.next = l.pop()
            head = head.next
        return result