# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
#     if root: 
#         root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
#     return root

def invert(self, root):
    if not root:
        return
    root.left, root.right = root.right, root.left
    self.invert(root.left)
    self.invert(root.right)
    
    return root

def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return root
    return self.invert(root)