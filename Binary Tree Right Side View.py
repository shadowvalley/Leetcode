# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from queue import Queue
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = Queue()

        rightView = []
        if not root:
            return rightView

        if root:
            queue.put(root)
            while not queue.empty():
                q = deque()
                size = queue.qsize()

                for i in range(size):
                    node = queue.get()

                    q.appendleft(node.val)

                    if node.left is not None:
                        queue.put(node.left)
                    if node.right is not None:
                        queue.put(node.right)  

                rightView.append(q.popleft())

        return rightView
        