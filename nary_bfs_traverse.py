class NewNode:
    def __init__(self,root):
        self.val = root
        self.child= []

class bfs:
    res = 0
    def traverse(self,r):
        queue = []
        if r:
            queue.append(r)
        while len(queue)>0:
            data = queue.pop(0)
            self.res +=data.val
            for i in range(len(data.child)):
                    queue.append(data.child[i])

        return self.res



if __name__ == '__main__':
    root = NewNode(1)
    root.child.append(NewNode(2))
    root.child.append(NewNode(3))
    root.child.append(NewNode(4))
    root.child[0].child.append(NewNode(5))
    root.child[0].child[0].child.append(NewNode(10))
    root.child[0].child.append(NewNode(6))
    root.child[0].child[1].child.append(NewNode(11))
    root.child[0].child[1].child.append(NewNode(12))
    root.child[0].child[1].child.append(NewNode(13))
    root.child[2].child.append(NewNode(7))
    root.child[2].child.append(NewNode(8))
    root.child[2].child.append(NewNode(9))
    b = bfs()
    print(b.traverse(root))