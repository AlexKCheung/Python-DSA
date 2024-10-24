# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def maxPathSum(self, root: Optional[TreeNode]) -> int:
    max_path = [root.val] # [] for global variable

    def depth(root):
        if not root:
            return 0
        left_max = max(0, depth(root.left))
        right_max = max(0, depth(root.right))

        max_path[0] = max(max_path[0], root.val + left_max + right_max)
        return root.val + max(left_max, right_max)
    
    depth(root)
    return max_path[0]