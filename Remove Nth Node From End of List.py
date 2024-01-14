# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = self.length(head)

        if length == 1:
            return head.next

        k = 0
        prev, dummy = None, head
        while k<(length-n):
            prev = dummy
            dummy = dummy.next
            k+=1

        if prev is None:
            return dummy.next

        # Change pointers
        if prev:
            prev.next = dummy.next
            del(dummy)

        return head

    def length(self, head: Optional[ListNode]) -> int:
        dummy = head
        length = 0
        while dummy:
            length += 1
            dummy = dummy.next
        return length