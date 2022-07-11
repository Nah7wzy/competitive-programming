# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque([root])
        
        while q:
            for i in range(len(q)):                
                curr = q.popleft()
                if curr and curr.left:
                    q.append(curr.left)
                if curr and curr.right:
                    q.append(curr.right)
            if curr:        
                res.append(curr.val)
            
        return res