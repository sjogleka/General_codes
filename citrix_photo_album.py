
'''
for i in range(len(a)):
    c.insert(a[i],b[i])
print(c)
'''
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def photoAlbum(index, identity):
    head = Node(identity.pop(0))
    index.pop(0)
    while identity:
        i = index.pop(0) - 1
        if i == -1:
            temp = Node(identity.pop(0))
            temp.next = head
            head = temp
            continue
        temp = head
        while i > 0:
            temp = temp.next
            i -= 1;
        new_node = Node(identity.pop(0))
        new_node.next = temp.next
        temp.next = new_node
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out

if __name__ == '__main__':
    n = 2
    a = [0, 1, 0]
    b = [0, 1, 2]
    print(photoAlbum(a,b))