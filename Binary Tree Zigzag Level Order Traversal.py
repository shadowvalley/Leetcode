# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from queue import Queue
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = Queue()
        zigZagLevelOrder = [] 

        if not root:
            return zigZagLevelOrder

        direction = True
        q.put(root)
        while not q.empty():
            size = q.qsize()
            deq = deque()

            for i in range(size):
                root = q.get()

                if direction:
                    deq.append(root.val)
                else:
                    deq.appendleft(root.val)

                if root.left:
                    q.put(root.left)
                if root.right:
                    q.put(root.right)

            zigZagLevelOrder.append(list(deq))
            direction = not direction

        return zigZagLevelOrder
