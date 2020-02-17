class Node:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class traversals:
    def inorder_traversal(self,root):
        def helperinorder(root,res):
            if root:
                helperinorder(root.left,res)
                res.append(root.val)
                helperinorder(root.right,res)

        res=[]
        helperinorder(root,res)
        return res

    def preorder_traversal(self,root):
        def helperpreorder(root,res):
            if root:
                res.append(root.val)
                helperpreorder(root.left,res)
                helperpreorder(root.right,res)

        res=[]
        helperpreorder(root,res)
        return res

    def postorder_traversal(self,root):
        def helperpostorder(root,res):
            if root:
                helperpostorder(root.left,res)
                helperpostorder(root.right,res)
                res.append(root.val)

        res=[]
        helperpostorder(root,res)
        return res




if __name__ == '__main__':
    root = Node(1)
    root.left =Node(2)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right = Node(3)

    #------------- Traversal -----------#
    treaverse = traversals()
    print("Pre order traversal: -",treaverse.preorder_traversal(root))
    print("In order traversal: -",treaverse.inorder_traversal(root))
    print("Post order traversal: -",treaverse.postorder_traversal(root))
