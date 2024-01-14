# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isTreeBST(root, -float('inf'), float('inf'))

    def isTreeBST(self, root: Optional[TreeNode], left, right):
        if not root:
            return True
        if root.val <= left or root.val >= right:
            return False
        return self.isTreeBST(root.left, left, root.val) and self.isTreeBST(root.right, root.val, right)
        