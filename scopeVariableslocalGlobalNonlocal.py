x , y ,z = 'globlal - x','global - y','global - z'


def basic_scoping():
    print(x)
    y = 'local - y'
    print(y)
    global z
    print(z)

def inner_outer_scope():
    def inner1():
        print(x)

    def inner2():
        x = 'inner2 - x'
        print(x)

    def inner3():
        nonlocal x
        x = 'inner3 - x'
        print(x)

    #print(x) #Error
    x = 'inner1 - x'
    print(x)
    inner1(), inner2(), inner3()
    print(x)







if __name__ == '__main__':
    basic_scoping()
    inner_outer_scope()
    x = 1000
    y = 499 + 501

    print(x is y)

    s1 = "Real Python!"
    s2 = "Real Python!"

    print(s1 is s2)