# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        slow = head
        fast = head.next
        for i in range(n):
            fast = fast.next
        while fast.next != None:
           fast = fast.next
           slow = slow.next
        fast.next = fast.next.next
        return head