# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from queue import Queue

class Solution:
    def markParent(self, root: Optional[TreeNode], parentMapper) -> None:
        q = Queue()

        q.put(root)
        while not q.empty():
            size = q.qsize()

            for i in range(size):
                node = q.get()
                if node.left:
                    q.put(node.left, node)
                    parentMapper[node.left.val] = node
                if node.right:
                    q.put(node.right, node)
                    parentMapper[node.right.val] = node

    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        parentMapper = {}
        self.markParent(root, parentMapper)

        # print("parentMapper - ", parentMapper)
        # for k, v in parentMapper.items():
        #     print(f"{k} - {v.val}")

        q = Queue()
        q.put(root)

        while not q.empty():
            size = q.qsize()
            level = []
            for i in range(size):
                node = q.get()
                level.append(node.val)

                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
            if x in level and y in level:
                # check for parent
                if parentMapper[x] != parentMapper[y]:
                    return True
                else:
                    return False
            if x in level or y in level:
                return False
