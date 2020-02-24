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
            if data[0].val:
                self.res.append((data[0].val,data[1]))
                if data[0].left:
                    queue.append((data[0].left,level+1))
                if data[0].right:
                    queue.append((data[0].right,level+1))
                level+=1
        return self.res

class bfs2:
    def traverser2(self,r):
        res= []
        queue = []
        if r:
            queue.append(r)
        while queue:
            data = queue.pop(0)
            res.append(data.val)
            print(res)
            if data.left:
                queue.append(data.left)
            if data.right:
                queue.append(data.right)

        return res


if __name__ == '__main__':
    root = Node(3)
    root.left = Node(9)
    root.right = Node(20)
    root.left.left = Node(15)
    root.left.right = Node(7)
    root.left.left.left = Node(10)
    root.left.left.right = Node(10)
    traverse = bfs()
    t = traverse.oddsum(root)
    #print(t)

    traverse2 = bfs2()
    t = traverse2.traverser2(root)
    print(t)

'''
    res = [[]]
    for i in range(len(t)):
        if len(res)-1==t[i][1]:
            res[t[i][1]].append(t[i][0])
        else:
            res.append([])
            res[t[i][1]].append(t[i][0])
        print(res)
'''