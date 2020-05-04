from collections import deque
'''
class FirstUnique:
    def __init__(self, nums):
        self.q = deque()
        self.s = set()
        self.array = []
        for i in range(len(nums)):
            if nums[i] not in self.s:
                self.s.add(nums[i])
                self.q.append(nums[i])
            elif nums[i] in self.s:
                self.s.remove(nums[i])
                self.q.remove(nums[i])

        print(self.q,self.s)

    def showFirstUnique(self):
        if not self.s:
            return -1
        print(self.q, self.s)
        temp = self.q[0]
        return temp


    def add(self, value):
        if value in self.s:
            self.s.remove(value)
            self.q.remove(value)
            return -1
        if value not in self.s:
            self.s.add(value)
            self.q.append(value)

'''
class Node:
    def __init__(self,value):
        self.value  = value
        self.prev = None
        self.next = None


class FirstUnique:
    def __init__(self, nums):
        self.d = {}
        self.s = set()
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        for i in range(len(nums)):
            if nums[i] not in self.s:
                node = Node(nums[i])
                self.addLL(node)
                self.d[nums[i]] = node
                self.s.add(nums[i])
            elif nums[i] in self.s:
                if nums[i] in self.d:
                    node2delete = self.d[nums[i]]
                    self.removeLL(node2delete)
                    del self.d[nums[i]]

    def addLL(self,node):
        temp = self.tail.prev
        node.next = self.tail
        self.tail.prev = node
        temp.next = node
        node.prev = temp

    def removeLL(self,node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def printLL(self):
        node = self.head
        res = []
        while node:
            res.append(node.value)
            node = node.next
        print("Current LL:- ",res)

    def showFirstUnique(self):
        self.printLL()
        return self.head.next.value


    def add(self, value):
        if value not in self.s:
            node = Node(value)
            self.addLL(node)
            self.d[value] = node
            self.s.add(value)
        elif value in self.s:
            if value in self.d:
                node2delete = self.d[value]
                self.removeLL(node2delete)
                del self.d[value]







if __name__ == '__main__':
    # Your FirstUnique object will be instantiated and called as such:
    '''
    obj = FirstUnique([7,7,7,7,7,7])
    param_1 = obj.showFirstUnique()
    print(param_1)
    obj.add(7)
    obj.add(3)
    obj.add(3)
    obj.add(7)
    obj.add(17)
    param_2 = obj.showFirstUnique()
    print(param_2)
    ########################################
    obj = FirstUnique([2,3,5])
    print(obj.showFirstUnique())
    obj.add(5)
    print(obj.showFirstUnique())
    obj.add(2)
    print(obj.showFirstUnique())
    obj.add(3)
    print(obj.showFirstUnique())
    '''
    obj = FirstUnique([809])
    print(obj.showFirstUnique())
    obj.add(809)
    print(obj.showFirstUnique())





