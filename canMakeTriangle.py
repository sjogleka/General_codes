def canMakeTriangle(arr):
    res = []
    for  i in range(len(arr)-2):
        if arr[i]+arr[i+1]>arr[i+2] and arr[i]+arr[i+2]>arr[i+1] and arr[i+1]+arr[i+2]>arr[i]:
            res.append(1)
        else:
            res.append(0)
    return res

if __name__ == '__main__':
    print(canMakeTriangle([1,2,2,4]))
    print(canMakeTriangle([2,10,2,10,2]))
    #print(canMakeTriangle([1000000000,])