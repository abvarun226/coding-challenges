# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.tree = []
        if root:
            self.inorder(root)
        return self.tree
        
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            self.tree.append(root.val)
            self.inorder(root.right)