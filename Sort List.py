# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Find middle node
        if head is None or head.next is None:
            return head

        tortoise = head
        hare = head.next

        while hare and hare.next:
            tortoise = tortoise.next
            hare = hare.next.next

        head2 = tortoise.next
        tortoise.next = None

        l1 = self.sortList(head)
        l2 = self.sortList(head2)
        return self.mergeTwoLists(l1, l2)

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        h1 = list1
        h2 = list2
        nhead = ListNode(-1)
        temp = nhead

        while h1 and h2:
            if h1.val <= h2.val:
                temp.next = h1
                h1 = h1.next
            else:
                temp.next = h2
                h2 = h2.next
            temp = temp.next
        
        # if some list is still not consumed
        while h1:
            temp.next = h1
            temp = temp.next
            h1 = h1.next

        while h2:
            temp.next = h2
            temp = temp.next
            h2 = h2.next
        return nhead.next