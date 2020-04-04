def cerealSegment(x,arr):
    b = []
    for i in range(len(arr)-x+1):
        v = []
        for j in range(i,i+x):
            v.append(arr[j])
        v = sorted(v)
        b.append(v[0])
    b = sorted(b,reverse=True)
    print(b[0])

if __name__ == '__main__':
    arr = [8, 2, 4]
    cerealSegment(2,arr)


