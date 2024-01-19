# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        stack = []
        stack.append(root)
        if not root:
            return root
        while len(stack) > 0:
            root = stack.pop()

            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
            
            if len(stack) > 0:
                root.right = stack[-1]
                root.left = None
        return root