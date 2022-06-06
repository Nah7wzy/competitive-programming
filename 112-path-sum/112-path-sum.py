# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:    return False
        
        def dfs(node):
            if not node.left and not node.right:    return node.val == targetSum
            left = right = None
            if node.left:
                node.left.val += node.val
                left = dfs(node.left)
            if node.right:
                node.right.val += node.val
                right = dfs(node.right)
               
            return left or right
        
        return dfs(root)
                