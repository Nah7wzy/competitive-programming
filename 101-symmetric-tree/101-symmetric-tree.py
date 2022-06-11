# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right:
            return True

        def bfs(left, right):
            if not left or not right:
                return not left and not right
            
            if left.val == right.val:
                return bfs(left.left, right.right) and bfs(left.right, right.left)
            else:
                return False
            
        return bfs(root.left, root.right)