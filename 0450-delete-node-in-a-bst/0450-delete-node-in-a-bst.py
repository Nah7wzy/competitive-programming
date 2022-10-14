# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def find_suc(node):
            if node.right:
                node = node.right
                while node and node.left:
                    node = node.left
            return node.val
                    
        def delete(node, val):
            if not node:
                return None
            if val > node.val:
                node.right = delete(node.right, val)
            elif val < node.val:
                node.left = delete(node.left, val)
            else:
                if not node.right and not node.left:
                    node = None
                elif node.right:
                    node.val = find_suc(node)
                    node.right = delete(node.right, node.val)
                else:
                    node = node.left
            return node
        
        return delete(root, key)