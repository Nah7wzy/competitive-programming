# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = dummy = ListNode(None, head)
        
        if not head: return head
        curr = head
        check = curr.next
        
        while curr and curr.next:
            if curr.val == check.val:
                if check.next and check.next.val == curr.val:
                    check=check.next
                    continue
                else:
                    prev.next, curr = check.next, check.next
                    if curr:
                        check = curr.next
                # prev = prev.next
                
            else:
                curr, check, prev = curr.next, check.next, prev.next
                
        return dummy.next