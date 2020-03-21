class ListNode:
    def __init__(self,x):
        self.val = x
        self.next  =None

class LinkedList:

    def __init__(self):
        self.head =  None


    def addFirst(self,x):
        new_node = ListNode(x)
        new_node.next  = self.head

        self.head = new_node

    def printAll(self):
        last = self.head
        while last:
            print(last.val)
            last = last.next

    def push(self,x):
        new_node = ListNode(x)
        new_node.next= None
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def reverseLL(self):
        prev = None
        curr = self.head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        self.head = prev


        '''
        prev = None
        current = self.head
        while current is not None:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        self.head = prev
        '''



if __name__ == '__main__':
    l = LinkedList()

    l.addFirst(1)
    l.addFirst(2)
    l.addFirst(3)
    l.addFirst(4)
    l.push(5)
    l.printAll()
    print("---------------------")
    l.reverseLL()
    l.printAll()
