# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        traversal = []
        def inOrder(node):
            if node is None:
                return
            inOrder(node.left)
            traversal.append(node)
            inOrder(node.right)
        
        inOrder(root)

        order = sorted(traversal, key=lambda x:x.val)
        for i in range(len(traversal)):            
            if traversal[i] != order[i]:
                traversal[i].val, order[i].val = order[i].val, traversal[i].val
                break