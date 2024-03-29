# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur_val = root.val
        
        if p.val > cur_val and q.val > cur_val:
            return self.lowestCommonAncestor( root.right, p, q)
        
        elif p.val < cur_val and q.val < cur_val:
            return self.lowestCommonAncestor( root.left, p, q)
        
        else:
            return root