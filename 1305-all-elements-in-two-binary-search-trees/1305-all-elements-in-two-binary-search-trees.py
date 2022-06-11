# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        ans = []
        
        def dfs(node):
            if not node:
                return
            
            if node.val <= 100000:
                ans.append(node.val) 
                
            node.val == 100001
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
                
        dfs(root1)
        dfs(root2)
        
        ans.sort()
        return ans