class Node:
    def __init__(self,root):
        self.val = root
        self.left = None
        self.right = None




class bfs:
    res = []
    def oddsum(self,root):
        queue = []
        level = 0
        if root:
            queue.append((root,level))

        while len(queue)>0:
            data = queue.pop(0)
            print(data[1])
            if data[1]%2!=0:
                self.res.append(data[0].val)
            if data[0].left:
                queue.append((data[0].left,level+1))
            if data[0].right:
                queue.append((data[0].right,level+1))

            level+=1

        print(self.res)



if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    traverse = bfs()
    print(traverse.oddsum(root))
