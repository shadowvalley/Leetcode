# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from queue import Queue

class Solution:
    def getParent(self, root: TreeNode, parentMapper) -> None:
        q = Queue()
        q.put(root)
        while not q.empty():
            node = q.get()
            if node.left:
                parentMapper[node.left] = node
                q.put(node.left)
            
            if node.right:
                parentMapper[node.right] = node
                q.put(node.right)
        

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parentMapper = {}
        parentMapper[root] = None
        
        # set parent for every node in the tree
        self.getParent(root, parentMapper)
        visited = set()

        q = Queue()
        q.put(target)
        visited.add(target)

        cur_level = 0
        while not q.empty():
            qsize = q.qsize()
            if cur_level == k:
                break

            cur_level += 1
            for i in range(qsize):
                curr = q.get()
                if curr.left and curr.left not in visited:
                    q.put(curr.left)
                    visited.add(curr.left)
                
                if curr.right and curr.right not in visited:
                    q.put(curr.right)
                    visited.add(curr.right)

                if parentMapper[curr] and parentMapper[curr] not in visited:
                    q.put(parentMapper[curr])
                    visited.add(parentMapper[curr])
    
        # Now, q will have all nodes at level k
        levelKNodes = []
        while not q.empty():
            levelKNodes.append(q.get().val)

        return levelKNodes
