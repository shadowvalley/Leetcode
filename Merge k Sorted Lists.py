# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Pair:
    def __init__(self, value, node):
        self.value = value
        self.node = node

    def __lt__(self, other):
        return self.value < other.value

import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        for l in lists:
             if l:
                heapq.heappush(heap, Pair(l.val, l))
        
        dummy = ListNode(-1)
        temp = dummy
        while len(heap)!=0:
            pr = heapq.heappop(heap)

            temp.next = pr.node
            temp = temp.next
            if pr.node.next:
                heapq.heappush(heap, Pair(pr.node.next.val, pr.node.next))

        return dummy.next