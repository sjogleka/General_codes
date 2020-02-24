class Node:
    def __init__(self,root):
        self.val = root
        self.left = None
        self.right = None

class bfs:
    res = []
    def traverse(self,r):
        queue = []
        if r:
            queue.append(r)
        while len(queue)>0:
            data = queue.pop(0)
            self.res.append(data.val)
            if data.left:
                queue.append(data.left)
            if data.right:
                queue.append(data.right)

        return self.res

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    traverse = bfs()
    print(traverse.traverse(root))
