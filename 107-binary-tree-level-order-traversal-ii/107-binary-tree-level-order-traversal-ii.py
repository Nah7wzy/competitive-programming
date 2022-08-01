# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        q = deque([root])
        if root:
            while q:
                temp = []
                for i in range(len(q)):
                    node = q.pop()
                    temp.append(node.val)
                    if node.left:
                        q.appendleft(node.left)
                    if node.right:
                        q.appendleft(node.right)
                levels.append(temp)
            
        return levels[::-1]