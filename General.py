def findFirst1(arr,tatget):
    def helper(start,end,target):
        mid = (start+end)//2
        if end>=start:
            if arr[mid]==target and arr[mid-1]!=target:
                return mid
            elif arr[mid]>=target:
                return helper(start,mid-1,tatget)
            elif arr[mid]<tatget:
                return helper(mid+1,end,tatget)
        else:
            return -1
    print(helper(0,len(arr),tatget))


def findFisrtANdLast(arr,target):
    def helper(lo,hi,left):
        found = -1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if target > arr[mid]:
                lo = mid + 1
            elif target < arr[mid]:
                hi = mid - 1
            else:
                if left:
                    found = mid
                    hi = mid - 1
                else:
                    found=mid
                    lo = mid+1

        return found

    l = helper(0,len(arr)-1,True)
    r = helper(0,len(arr)-1,False)

    print(l,r)

class Node:
    def __init__(self,x):
        self.val = x
        self.next = None

class Node1:
    def __init__(self,root):
        self.left = None
        self.val = root
        self.right = None

def inetraverse(root):
    def helper(r, res):
        if r:
            helper(r.left,res)
            res.append(r.val)
            helper(r.right,res)


    res =[]
    helper(root,res)
    print(res)

def bfs(root):
    q= []
    q.append(root)
    res =[]
    while q:
        data = q.pop(0)
        res.append(data.val)
        if data.left:
            q.append(data.left)
        if data.right:
            q.append(data.right)

    print(res)

def over1(a,b,c):
    return a+b+c

def over1(a,b,c,d):
    return a+b+c+d

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self,x):
        new_node = Node(x)
        if not self.head:
            self.head = new_node

        last = self.head
        while last.next:
            last= last.next

        last.next = new_node
        new_node.next = None

    def start(self,x):
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node

    def printAll(self):
        temp = self.head
        print("Printing ..... ")
        while temp:
            print(temp.val)
            temp = temp.next

    def delete(self,x):
        prev = None
        curr = self.head

        while curr.val!=x:
            nxt = curr.next
            prev = curr
            curr = nxt

        prev.next = curr.next

    def reverseLL(self):
        prev = None
        curr = self.head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        self.head = prev


    def middle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        print("Middle Element: -",slow.val)


def Sum35():
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        i = 1
        sum = 0
        while (i < n):
            mof3 = 3 * i
            mof5 = 5 * i
            if mof3 < n:
                sum = sum + mof3
            if mof5 < n and mof5 % 3 != 0:
                sum = sum + mof5
            i = i + 1
        print(sum)

if __name__ == '__main__':
    #findFirst1([0, 0, 0, 0, 0, 0, 1, 1, 1, 1],1)
    #findFisrtANdLast([5,7,7,8,8,10],8)
    #findFisrtANdLast([5, 7, 7, 8, 8, 10,10,10,10,10,11,13,15], 10)
    #findFisrtANdLast([5, 7, 7, 8, 8, 10, 10, 10, 10, 11, 13, 15], 16)
    #findFisrtANdLast([5,7,7,8,8,10], 6)
    '''
    root = Node1(1)
    root.left = Node1(2)
    root.right = Node1(3)
    root.left.left = Node1(4)
    root.left.right = Node1(5)
    root.right.left = Node1(6)
    root.right.right = Node1(7)
    root.right.left.left = Node1(8)
    inetraverse(root)
    #bfs(root)'''
    '''
    l = LinkedList()
    l.push(2)
    l.push(3)
    l.push(4)
    l.push(1)
    l.start(5)
    l.start(6)
    l.delete(2)
    l.printAll()
    l.reverseLL()
    l.printAll()
    l.middle()
    
    print(over1(1,3,3))
    print(over1(1, 3, 3,4))
    '''

    #Sum35()

    d= {True:"yes",1.0:"maybe",1:"no"}
    print(d)
    d = {True: "yes", 1: "no", 1.0: "maybe"}
    print(d)


