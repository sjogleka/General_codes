
class Node:
    def __init__(self,root):
        self.left = None
        self.val = root
        self.right = None

class traverse:
    res = 0
    def sumOfNodes(self,r):
        if r:
            self.sumOfNodes(r.left)
            #print(root.val)
            #res.append(r.val)
            self.res+= r.val
            print("--------",self.res)
            if self.res%2!=0:
                print(self.res,r.val)
            self.sumOfNodes(r.right)
            return self.res
        else:
            return 0





if __name__ == '__main__':
    op =[]
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.right.left.right = Node(8)
    tr = traverse()
    op = tr.sumOfNodes(root)
    #print(op)