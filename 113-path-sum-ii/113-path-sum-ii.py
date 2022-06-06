# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        total = 0
        res = []

        def dfs(node, prefixSum, temp=[]):
            if not node:    return
            
            temp.append(node.val)
            prefixSum += node.val
            if not node.left and not node.right:    
                if prefixSum == targetSum:
                    res.append(temp[:])
                    
                temp.pop()
                prefixSum -= node.val
                return
            
            dfs(node.left, prefixSum, temp)
            dfs(node.right, prefixSum, temp)
            temp.pop()
        
        dfs(root, total)
        return res