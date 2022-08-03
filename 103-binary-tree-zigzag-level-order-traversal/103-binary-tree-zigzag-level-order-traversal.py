# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        queue = deque([root])
        flag = False
        if root:
            while queue:
                count = len(queue)
                temp = []
                while count > 0:
                    node = queue.popleft()
                    temp.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                    count -= 1
                if flag:
                    levels.append(temp[::-1])
                else:
                    levels.append(temp)
                flag = not flag
            
        return levels