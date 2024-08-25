# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
    output_list = []

    # dfs 
    def next_node(root, curSum, targetSum, path):
        if root:
            if root.val + curSum == targetSum and not root.left and not root.right:
                path.append(root.val)
                output_list.append(path)
            next_node(root.left, root.val + curSum, targetSum, path + [root.val])
            next_node(root.right, root.val + curSum, targetSum, path + [root.val])

    next_node(root, 0, targetSum, [])
    return output_list