# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaves_root1 = []
        self.getAllLeaves(root1, leaves_root1)

        leaves_root2 = []
        self.getAllLeaves(root2, leaves_root2)
        
        return True if leaves_root1 == leaves_root2 else False

    def getAllLeaves(self, root: Optional[TreeNode],leaves: List[int]) -> List[int]:
        if not root:
            return leaves
        
        if root.left is None and root.right is None:
            leaves.append(root.val)
        self.getAllLeaves(root.left, leaves)
        self.getAllLeaves(root.right, leaves)
