

class Node:

    def __init__(self,root):
        self.val = root
        self.left = None
        self.right = None



def findSum(root):
    def helper(r,level):
        if r:
            print(level_sum)
            helper(r.left,level+1)
            if level in level_sum:
                level_sum[level]+=r.val
            else:
                level_sum[level]=r.val
            helper(r.right,level+1)

    level_sum = {}
    helper(root,1)
    print(level_sum)

    return max(level_sum)



if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.right.left.left = Node(8)

    print(findSum(root))
