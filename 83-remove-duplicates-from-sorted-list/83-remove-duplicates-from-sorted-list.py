# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = dummy = ListNode(0)
        dummy.next = head
        ptr=dummy.next
        
        app = []
        while ptr:
            if ptr.val not in app:
                app.append(ptr.val)
                ptr=ptr.next
                prev=prev.next
                
            elif ptr.val in app:
                prev.next = ptr.next                
                ptr=ptr.next
               # print(ptr, prev)
                
        return dummy.next
                