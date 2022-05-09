# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res=ListNode()
        ptr = head
        while ptr:
            trv = res #to traverse from the first
            while trv.next and trv.next.val < ptr.val:
                trv = trv.next #breaks when finding the spot
                
            #then operate on the spot (simultaneously to avoid using temp)
            trv.next, ptr.next, ptr = ptr, trv.next, ptr.next
            
        return res.next
            