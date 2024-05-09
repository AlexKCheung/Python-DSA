# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    output = []
    # left, middle, right

    def bfs(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return None
        if root.left != None:
            bfs(self, root.left)

        output.append(root.val)

        if root.right != None:
            bfs(self, root.right)
        return None
        
    bfs(self, root)
    return output