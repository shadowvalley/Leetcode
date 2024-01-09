# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from queue import Queue

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levelOrder = []
        if not root:
            return levelOrder
        q = Queue()
        q.put(root)
        while not q.empty():
            size = q.qsize()
            temp = []
            for i in range(size):
                root = q.get()
                temp.append(root.val)

                if root.left:
                    q.put(root.left)
                if root.right:
                    q.put(root.right)
            
            levelOrder.append(list(temp))
        return levelOrder
        