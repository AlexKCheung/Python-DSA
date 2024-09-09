# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []
    output, level = [], [root]
    while level:
        cur_node = []
        next_level = []
        for node in level:
            cur_node.append(node.val)
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        output.append(cur_node)
        level = next_level

    return output