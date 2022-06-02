# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        
        if not lists:   return ListNode('')
        
        for i in range(len(lists)):
            if lists[i]:
                heap.append((lists[i].val, i, lists[i]))   #i to avoid heapify using the linked list 
                                                           #when first values are similar       
        heapify(heap)
        
        dummy = ans = ListNode(None)
        #use tuple of list first value and the linked list which gets traversed on each heappush
        while heap:
            x = heappop(heap)
            ans.next = ListNode(x[0])
            ans = ans.next
            
            if not x[2].next:
                if len(heap) == 0:  break
            else:
                heappush(heap, (x[2].next.val, x[1], x[2].next))
            
            
        return dummy.next