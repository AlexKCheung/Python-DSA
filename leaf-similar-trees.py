# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

    def reach_end(root):
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]
        return reach_end(root.left) + reach_end(root.right)

    return reach_end(root1) == reach_end(root2)
