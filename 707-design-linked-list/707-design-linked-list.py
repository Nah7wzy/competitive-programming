class ListNode:
    def __init__(self, next=None, val=None):
        self.next = next
        self.val = val
        
class MyLinkedList:

    def __init__(self):
        self.head=ListNode()
        self.size=0
    def get(self, index: int) -> int:
        if (index >= self.size):
            return -1
        ptr = self.head
        for i in range(index):
            ptr = ptr.next
        return ptr.val

    def addAtHead(self, val: int) -> None:
        if (self.size == 0):
            self.head.val = val
        else:
            node = ListNode(next=self.head, val=val)
            self.head = node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        if (self.size == 0):
            self.addAtHead(val)
        else:
            ptr = self.head
            while (ptr.next != None):
                ptr = ptr.next
            ptr.next = ListNode(val=val)
            self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if (index > self.size):
            return
        elif (index == 0):
            self.addAtHead(val)
        elif (index == self.size):
            self.addAtTail(val)
        else:
            ptr = self.head
            for i in range(index-1):
                ptr = ptr.next
            node = ListNode(next=ptr.next, val=val)
            ptr.next = node
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index<self.size:
            if index==0:
                self.head = self.head.next
            else:
                temp = self.head
                prev = self.head
                for i in range(index):
                    prev = temp
                    temp = temp.next
                prev.next = temp.next
            self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)