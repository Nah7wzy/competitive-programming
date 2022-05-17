# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        l=r=head
        #find mid
        while r and r.next: 
            r=r.next.next
            l=l.next
            
        prev , second = None, l
        
        #reverse second part
        while second:
            temp = second.next
            second.next = prev   #reverse
            prev = second
            second = temp
        
        #assign turn by turn
        first , second = head, prev
        
        while second.next:
            ln, rn = first.next, second.next #to save next iteration before change
            first.next, second.next = second, first.next
            first, second = ln, rn
            
        