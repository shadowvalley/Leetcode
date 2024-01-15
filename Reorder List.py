# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        middleNode = self.findListMiddle(head)
        head2 = middleNode.next
        middleNode.next = None
        nhead = self.reverse(head2)
        return self.alternateMergeLL(head, nhead)

    def findListMiddle(self, head: Optional[ListNode]):
        # Find first middle node
        t = head
        h = head.next

        while h and h.next:
            t = t.next
            h = h.next.next

        return t

    def reverse(self, head: Optional[ListNode]):
        prev, next = None, None
        cur = head

        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev

    def alternateMergeLL(self, headA: Optional[ListNode], headB: Optional[ListNode]):
        nhead = ListNode(-50)
        temp = nhead

        while headA and headB:
            temp.next = headA
            headA = headA.next
            temp = temp.next

            temp.next = headB
            headB = headB.next
            temp = temp.next

        if headA:
            temp.next = headA

        if headB:
            temp.next = headB
        return nhead.next
    