# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from queue import Queue
from collections import deque

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        largestValues = []
        if not root:
            return largestValues
        
        q = Queue()
        q.put(root)
        while not q.empty():
            size = q.qsize()
            level = deque()
            maxVal = -2**31-1
            for i in range(size):
                root = q.get()
                if root.val > maxVal:
                    maxVal = root.val
                    level.appendleft(maxVal)
                
                if root.left:
                    q.put(root.left)
                if root.right:
                    q.put(root.right)
            
            if level:
                largestValues.append(level[0])
        return largestValues
