'''
Level Order traversal of  N ary tree and reverse the level
'''
import  collections
class NewNode:
    def __init__(self,root):
        self.val = root
        self.child = []


def travverse(node):
    q = collections.deque()
    q.append(node)
    s = []
    while q:
        n = q.popleft()
        for i in range(len(n.child)):
            q.append(n.child[i])

        s.insert(0,n.val)

    print(s)



if __name__ == '__main__':
    root = NewNode('A')
    root.child.append(NewNode('B'))
    root.child.append(NewNode('C'))
    #root.child.append(NewNode(4))
    root.child[0].child.append(NewNode('D'))
    root.child[0].child[0].child.append(NewNode('H'))
    root.child[0].child.append(NewNode('E'))
    root.child[1].child.append(NewNode('F'))
    root.child[1].child.append(NewNode('G'))
    root.child[0].child[0].child[0].child.append(NewNode('I'))
    #root.child[0].child[1].child.append(NewNode(11))
    #root.child[0].child[1].child.append(NewNode(12))
    #root.child[0].child[1].child.append(NewNode(13))
    #root.child[2].child.append(NewNode(7))
    #root.child[2].child.append(NewNode(8))
    #root.child[2].child.append(NewNode(9))

    travverse(root)


