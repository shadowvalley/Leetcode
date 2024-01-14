# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Inorder traversal of BST gives a sorted array
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inorder = self.inorderTraversal(root)
        return inorder[k-1]
        
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        inorder = []
        if not root:
            return inorder

        stack = []
        while len(stack)!= 0 or root:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            inorder.append(root.val)
            root = root.right
        return inorder
        