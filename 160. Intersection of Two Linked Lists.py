# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        pA = headA
        pB = headB
        while pA != pB:
            if pA:
                pA = pA.next
            else:
                pA = headA
            if pB:
                pB = pB.next
            else:
                pB = headB
        return pA

    def getIntersectionNodeFull(self, headA, headB):
        countA = 0
        countB = 0
        pA = headA
        pB = headB
        while pA:
            pA = pA.next
            countA += 1
        while pB:
            pB = pB.next
            countB += 1
        pA = headA
        pB = headB
        maxIntersec = min(countA, countB)
        if maxIntersec == countA:
            for i in range(maxIntersec, countB):
                pB = pB.next
        else:
            for i in range(maxIntersec, countA):
                pA = pA.next
        while pA and pA != pB:
            pA = pA.next
            pB = pB.next
        return pA
