# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

    def reach_end(root, sum, targetSum):
        if root:
            if root.val + sum == targetSum and not root.left and not root.right:
                return True
            return reach_end(root.left, root.val + sum, targetSum) or reach_end(root.right, root.val + sum, targetSum)
        return False

    return reach_end(root, 0, targetSum)


