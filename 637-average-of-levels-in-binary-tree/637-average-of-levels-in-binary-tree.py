# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        levels = deque([root])
        res = []
        
        while levels:
            count = x = len(levels)
            total = 0
            while count > 0:
                node = levels.popleft()
                total += node.val
                if node.left:
                    levels.append(node.left)
                if node.right:
                    levels.append(node.right)
                count -= 1
                
            res.append(total / x)
            
        return res