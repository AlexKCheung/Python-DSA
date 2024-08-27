"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

def postorder(self, root: 'Node') -> List[int]:
    if not root:
        return []
    
    output = []
    def dfs(root):
        for i in root.children:
            dfs(i)
        output.append(root.val)
    dfs(root)
    return output