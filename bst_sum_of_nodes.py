
class Node:
    def __init__(self,root):
        self.left = None
        self.val = root
        self.right = None

class traverse:
    def sumOfNodes(self,r):
        res = 0
        if r:
            res+=self.sumOfNodes(r.left)+r.val+self.sumOfNodes(r.right)

        print("--------", res)
        return res

    def recursive(self,r):
        def helper(r,res):
            if r:
                helper(r.left, res)
                res.append(r.val)
                helper(r.right,res)
        res =[]
        helper(r,res)
        return res

    def iterative(self,r):
        queue = []
        res =[]
        if r:
            queue.append(r)
        while queue:
            data = queue.pop(0)
            res.append(data.val)
            if data.left:
                queue.append(data.left)
            if data.right:
                queue.append(data.right)

        return res

if __name__ == '__main__':
    op =[]
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.right.left.left = Node(8)
    tr = traverse()
    #op = tr.sumOfNodes(root.right)
    #print(op)

    #print(tr.recursive(root))
    print(tr.iterative(root))