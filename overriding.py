class A():
    def __init__(self):
        print("in A")

    def method1(self):
        print("Method 1 of A")

    def method2(self,a,b):
        print("method 2 of A")

class B(A):
    def __init__(self):
        print("in B")


    def method1(self):
        print("Method 1 of B")

    # Error
    def method2(self,a):
        print("method 2 of B")


if __name__ == '__main__':
    a = A()
    a.method1()
    a.method2(2,3)


    b = B()
    b.method1()
    #b.method2(5)
    b.method2(5,1)

