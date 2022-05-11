# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        #find mid and reverse second half of mid
        slow=head
        fast=head.next
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
            
        mid = slow
        
        prev, curr = None, mid.next
        while curr:
            temp = curr.next
            curr.next = prev   #reverse
            prev = curr
            curr = temp
        
        mid.next = prev
        
        ptr1 = head
        ptr2 = mid.next
        res=ptr1.val+ptr2.val
        while ptr1 and ptr2:
            if ptr1.val+ptr2.val > res:
                res = ptr1.val+ptr2.val
            ptr1=ptr1.next
            ptr2=ptr2.next
            
        return res