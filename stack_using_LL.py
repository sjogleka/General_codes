class Node:
    def __init__(self,val):
        self.val=val
        self.next = None
class stack:
    def __init__(self):
        self.root = None

    def push(self, data):
        newnode = Node(data)
        newnode.next = self.root
        self.root = newnode

    def pop(self):
        if (self.isempty()):
            return "-1"
        temp = self.root
        self.root = self.root.next
        popped = temp.val
        return popped

    def isempty(self):
        return True if self.root is None else False


if __name__ == '__main__':
    a = [1,2,3,6,3,8,4]
    node = []
    length = len(a)
    s = stack()
    for i in range(len(a)):
        s.push(a[i])
    for i in range(len(a)):
        print (s.pop())


    '''
    for i in range(len(a)):
        node.append(Node(a[i]))
        node[i-1].next = node[i]
    print(node)
    current = node[0]
    while current!=None:
        print(current.val)
        current = current.next
    '''