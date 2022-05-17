# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next: return head
        
        slow= fast = head
        while fast.next and fast.next.next:
            fast, slow = fast.next.next, slow.next
        
        mid = slow.next
        slow.next = None
        
        a, b = self.sortList(head), self.sortList(mid)
        
        resHead = ListNode(-1)
        res = resHead 
        while a or b:
            if not a or (b and a.val >= b.val):
                res.next, b = b, b.next
            else:
                res.next, a = a, a.next
            res = res.next
        
        res.next = None
        
        return resHead.next