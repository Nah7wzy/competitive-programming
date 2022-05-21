# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = 0 #to find the spot to reverse
        curr = head
        while curr and count<k:
            curr = curr.next
            count+=1
            
        if count<k: #means too short to reverse
            return head
        
        new_head, prev = self.helper(head, count)
        head.next = self.reverseKGroup(new_head, k)
        return prev
    
    
    def helper(self, head, i):
        prev=None
        ptr=head
        while ptr and i>0:
            temp=ptr.next 
            ptr.next=prev 
            prev=ptr 
            ptr=temp
            i-=1
        return (ptr, prev)
        
        
        
        
#reverse and attach next to a recursion function, use the i and k for the while loop inside helper