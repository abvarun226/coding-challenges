# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        result = {}
        q = [(0, root)]

        while len(q) > 0:
            t = q.pop(0)
            level = t[0]
            node = t[1]

            if level not in result:
                result[level] = []
            result[level].append(node.val)
            
            if node.left is not None:
                q.append((level+1, node.left))
            
            if node.right is not None:
                q.append((level+1, node.right))

        return list(result.values())