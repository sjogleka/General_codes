class Node:
    def __init__(self,root):
        self.val = root
        self.left =None
        self.right = None

from collections import defaultdict
def printAncestors(node,val):
    q = []
    parent  = defaultdict()
    if node:
        q.append(node)
        parent[node.val] = None
        while q:
            data = q.pop(0)
            if data.left:
                parent[data.left.val] = data.val
                q.append(data.left)
            if data.right:
                parent[data.right.val] = data.val
                q.append(data.right)
        print(parent)
    res = []
    while parent[val]:
        res.append(parent[val])
        val = parent[val]

    print(res)





if __name__ == '__main__':
    # Driver program to test above function
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.left.left = Node(7)

    printAncestors(root, 7)