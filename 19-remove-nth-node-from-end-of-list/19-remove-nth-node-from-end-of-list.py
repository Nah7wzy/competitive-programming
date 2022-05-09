# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        ptr1 = ptr2 = dummy
        
        if head.next == None and n==0: return head
        elif head.next == None and n==1:
            ptr2=None
            return ptr2
        
        count1 = count2 = 0
        while ptr1.next != None:
            count1 +=1
            ptr1=ptr1.next
            
        while count1 - count2!= n:
            count2+=1
            ptr2=ptr2.next
        
        ptr2.next=ptr2.next.next
        # print(count1, count2, ptr1, ptr2)   
        return dummy.next
        