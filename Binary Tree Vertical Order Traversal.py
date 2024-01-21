# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Pair:
    def __init__(self, node: Optional[TreeNode], idx: int):
        self.node = node
        self.idx = idx

from queue import Queue
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        verticalOrder = []
        if not root:
            return verticalOrder
        
        q = Queue()
        vertMapper = {}
        q.put(Pair(root, 0))
        while not q.empty():
            size = q.qsize()
            for i in range(size):
                pr = q.get()
                node = pr.node
                node_idx = pr.idx

                if node_idx not in vertMapper:
                    vertMapper[node_idx] = [node.val]
                else:
                    vertMapper[node_idx].append(node.val)

                if node.left:
                    q.put(Pair(node.left, node_idx-1))
                if node.right:
                    q.put(Pair(node.right, node_idx+1))
        sortedMapper = sorted(vertMapper.items())

        # for k,v in sortedMapper:
        #     verticalOrder.append(list(v))
        verticalOrder = [list(v) for k, v in sortedMapper]
        return verticalOrder