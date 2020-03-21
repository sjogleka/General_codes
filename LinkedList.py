class ListNode:
    def __init__(self,x):
        self.val = x
        self.next  =None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self,x):
        print("---- Pusing at end -----",x)
        new_node = ListNode(x)
        if not self.head:
            new_node.next = None
            self.head = new_node

        last = self.head
        while last.next:
            last= last.next

        last.next = new_node
        new_node.next = None

    def printAll(self):
        last = self.head
        op = []
        while last:
            op.append(last.val)
            last = last.next
        return op

    def length(self):
        last = self.head
        length = 0
        while last:
            length+=1
            last = last.next

        return length

    def addAtfirst(self,x):
        print("---- Adding at start -----",x)
        new_node = ListNode(x)
        new_node.next = self.head
        self.head = new_node

    def deleteNode(self,x):
        print("---- Deleting the node -----",x)
        prev = self.head
        targetNode = self.head
        if self.head.val ==x:
            self.head = self.head.next

        while targetNode.val != x:
            #print("---target---",targetNode.val)
            #print("----prev--", prev.val)
            prev = targetNode
            targetNode = targetNode.next
        prev.next = targetNode.next

if __name__ == '__main__':
    l = LinkedList()
    l2 = LinkedList()
    l.push(2)
    l.push(3)
    l.push(4)
    l.push(1)
    l2.addAtfirst(2)
    l2.addAtfirst(3)
    l2.addAtfirst(4)
    l2.addAtfirst(1)
    print(l.printAll())
    print(l2.printAll())
    print(l.length())
    l.deleteNode(4)
    print(l.printAll())
    l.addAtfirst(7)
    l.push(7)
    print(l.printAll())
    l.deleteNode(7)
    print(l.printAll())
    l.deleteNode(7)
    print(l.printAll())
