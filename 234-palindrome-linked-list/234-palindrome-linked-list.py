# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l,r=head, head.next
        #find mid
        while r and r.next: 
            r=r.next.next
            l=l.next
        
        prev , second = None, l.next
        #reverse second part
        while second:
            temp = second.next
            second.next = prev   #reverse
            prev = second
            second = temp
        second = prev
        first = head
        while second:
            if first.val!=second.val:
                return False
            first, second = first.next, second.next
            
        return True
        