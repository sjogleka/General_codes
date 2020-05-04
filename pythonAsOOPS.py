class A:
    def __init__(self):
        print("Initializing A")

    def method1(self,a,b):
        print(a,b)

class B(A):
    def __init__(self):
        print("Initializing B")

    def method1(self,a,b):
        print(a-b)


class C(B):
    def __init__(self):
        print("Initializing B")

    def method1(self,a,b,c):
        print(a,b,c)

class D:
    def __init__(self):
        print("Initializing C")

    def method1(self,a):
        print(a)

############### Multiple Inheritance ##############

class E(B,D):

    def __init__(self):
        print("Initializing E")

    def method1(self,a,b,c):
        print(a,b,c)

if __name__ == '__main__':
    a = A()
    b = B()
    c = C()
    e = E()
    a.method1(2,3)
    b.method1(2,3)
    c.method1(2,1,4)
    e.method1(1,2,3)
    print("Type of A",type(a))
    print("Class of A", type(a).__class__)
    print("MRO(Method Resolution Order): -", type(a).mro())
