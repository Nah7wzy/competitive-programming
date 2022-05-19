# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack = []
        res = []
        curr = head
        i = 0
        while curr:
            res.append(0)
            
            while stack and stack[-1][0] < curr.val:
                x = stack.pop()
                res[x[1]] = curr.val
                
            stack.append([curr.val, i])
                    
            curr = curr.next
            i+=1
            
        return res