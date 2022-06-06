# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        total = 0
        
        def dfs(node, prefixSum):
            if not node:    return False
            if not node.left and not node.right:    
                return node.val + prefixSum == targetSum
            prefixSum += node.val
            
            return dfs(node.left, prefixSum) or dfs(node.right, prefixSum)
        
        return dfs(root, total)
                