# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from queue import Queue

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = Queue()
        ans = []

        if not root:
            return ans 

        q.put(root)
        while not q.empty():
            size = q.qsize()

            temp = []
            for i in range(0, size):
                node = q.get()
                temp.append(node.val)

                if node.left is not None:
                    q.put(node.left)

                if node.right is not None:
                    q.put(node.right)

            tempSize = len(temp)
            tempSum = sum(temp)

            ans.append(tempSum/tempSize)
        return ans 


        