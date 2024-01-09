# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Base Cases
        if not subRoot:
            return True
        if not root:
            return False

        # Check if the current nodes are equal and their subtrees are also equal
        if root.val == subRoot.val and self.isSame(root.left, subRoot.left) and self.isSame(root.right, subRoot.right):
            return True
        
        # Check if the subtree is present in the left or right subtree
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)

        return left or right

    def isSame(self, node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:
        # Helper function to check if two subtrees are equal
        if not node1 and not node2:
            return True
        if not node1 or not node2:
            return False

        return node1.val == node2.val and self.isSame(node1.left, node2.left) and self.isSame(node1.right, node2.right)