# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorder(self, root):
        if root is not None:
            self.tree.append(root.val)
            self.preorder(root.left)
            self.preorder(root.right)

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        self.tree = []
        if root is not None:
            self.preorder(root)
        return self.tree
