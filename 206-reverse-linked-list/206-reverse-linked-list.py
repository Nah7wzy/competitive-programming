# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        ptr=head
        while ptr:
            temp=ptr.next #preserve the next since the current next will be changed to prev
            ptr.next=prev #point backwards
            prev=ptr #update prev to current (which also traverse)
            ptr=temp
        return prev #last previous will be the head of the reversed