# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        cols = defaultdict(list)
        
        def dfs(node, row, col):
            if not node:
                return
            
            cols[col].append([node.val, row])
            if node.left:
                dfs(node.left, row+1, col-1)
            if node.right:
                dfs(node.right, row+1, col+1)
                
        dfs(root, 0, 0)
        order = sorted(cols.keys())
        res = []
        
        for i in order:
            temp = [x for x in cols[i]]
            temp.sort(key = lambda x: (x[1], x[0]))
            res.append([y[0] for y in temp])
            
        return res
        