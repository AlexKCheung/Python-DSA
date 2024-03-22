# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def isBalanced(self, root: Optional[TreeNode]) -> bool:
    if root is None:
        return True
    left = self.returnHeight(root.left)
    right = self.returnHeight(root.right)
    if (abs(left - right) < 2) and self.isBalanced(root.left) and self.isBalanced(root.right):
        return True
    return False
    

def returnHeight(self, root):
    if root is None:
        return 0

    return max(self.returnHeight(root.left), self.returnHeight(root.right)) + 1

