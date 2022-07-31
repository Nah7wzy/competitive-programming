# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        count = 0
        monitored = {None}
        
        def dfs(node, parent = None):
            nonlocal count
            if not node:
                return
            
            dfs(node.left, node)
            dfs(node.right, node)
            
            if (parent is None and node not in monitored) or node.left not in monitored or node.right not in monitored:
                #if one of em is uncovered add a camera and consider all nodes in range covered 
                count += 1
                monitored.update({node, parent, node.left, node.right})
                
        dfs(root)
        return count