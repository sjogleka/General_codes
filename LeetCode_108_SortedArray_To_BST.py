class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortArrayToBST(self,ar):
        if len(ar)==0:
            return None
        mid = len(ar)//2
        r = TreeNode(ar[mid])
        r.left=self.sortArrayToBST(ar[:mid])
        r.right = self.sortArrayToBST(ar[mid+1:])

        return r

    def inOrder(self,root):
        def helper(root,res):
            if root:
                helper(root.left,res)
                res.append(root.val)
                helper(root.right,res)
            else:
                res.append("null")
        res = []
        helper(root, res)
        return res

    def preOrder(self,root):
        print(root)
        def helper(root,res):
            if root:
                res.append(root.val)
                helper(root.left,res)
                helper(root.right,res)

        res = []
        helper(root, res)
        return res

if __name__ == '__main__':
    s = Solution()
    arr = [-10,-3,0,5,9]
    print(s.inOrder(s.sortArrayToBST(arr)))
    print(s.preOrder(s.sortArrayToBST(arr)))
'''    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    '''
    #print(s.inOrder(root))
