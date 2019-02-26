# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        self.tree = []
        if root:
            self.postorder(root)
        return self.tree

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            self.tree.append(root.val)