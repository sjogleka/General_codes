def square(x,a):
    if a == 0:
        return 1
    if a ==1:
        return x

    return x*square(x,a-1)


if __name__ == '__main__':
    print(square(2,0))