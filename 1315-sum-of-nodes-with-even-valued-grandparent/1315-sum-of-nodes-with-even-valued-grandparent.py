# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        res = 0
        def dfs(node, p = 0, gp = 0):
            nonlocal res
            if node:
                if gp and gp % 2 == 0:
                    res += node.val
                dfs(node.left, node.val, p)
                dfs(node.right, node.val, p)
        
        dfs(root)
        return res