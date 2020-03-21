def appendZeroAtEnd(arr):
    #temp = [1,0,2,3,0,4,5]
    ptr  = 0
    for i in range(len(arr)):
        if arr[i]!=0:
            arr[ptr]=arr[i]
            ptr+=1
    for i in range(ptr,len(arr)):
        arr[i] = 0
    print(arr)


if __name__ == '__main__':
    arr = [1,0,2,3,0,4,5]
    arr1 = [0, 2, 3, 0, 4, 5]
    arr2 = []
    arr3 = [0, 0, 0, 0]
    appendZeroAtEnd(arr)
    appendZeroAtEnd(arr1)
    appendZeroAtEnd(arr2)
    appendZeroAtEnd(arr3)

