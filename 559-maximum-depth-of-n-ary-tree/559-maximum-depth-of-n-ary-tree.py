"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        res = 0
        def dfs(node, depth):
            nonlocal res
            if node:
                depth += 1
                res = max(res, depth)
                for child in node.children:
                    dfs(child, depth)
        dfs(root, res)  
        return res