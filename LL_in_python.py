class Node:
    def __init__(self,data):
        self.data = data;
        self.next = None;


n1 = Node(21);
n2 = Node(22);

n1.next = n2;

print(n1.data,n2.data)

a = [1,2,4,6,8,9,1]
print(a)
a.sort()
print("Pop :- ",a.pop(3))
print(a)
a.reverse()
print("Reverse :-",a)
