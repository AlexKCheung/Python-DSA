# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    stack = collections.deque()
    if root:
        stack.append(root)
    output = []

    while stack:
        current_level = []
        for i in range(len(stack)):
            a = stack.popleft()
            current_level.append(a.val)
            if a.left:
                stack.append(a.left)
            if a.right:
                stack.append(a.right)

        output.append(current_level)            
    
    return output
    
