# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        @cache
        def dfs(node, chosen):
            if not node:
                return 0
            choose = 0
            if not chosen:
                choose = node.val + dfs(node.left, 1) + dfs(node.right, 1)
            
            skip = dfs(node.left, 0) + dfs(node.right, 0)
            res = 0
            res = res + max(choose, skip)
            return res
        return dfs(root, 0)
        
            