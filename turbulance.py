def findTurbulance(arr,idx,res):
    for j in range(idx,len(arr)-2):
        if arr[j]>arr[j+1] and arr[j+1]<arr[j+2]:
            res.append(j)
            res.append(j+1)
            res.append(j + 2)
            #res.append(arr[j])
            #res.append(arr[j+1])
            #res.append(arr[j+2])
            findTurbulance(arr,j+2,res)
        else:
            break


if __name__ == '__main__':
    #arr = [9,4,2,10,7,8,8,1,9]
    arr = [9, 4, 2, 10, 7, 8, 8, 1, 9]
    maxRange = [0,0]
    for i in range(len(arr)):
        res = []
        findTurbulance(arr,i,res)
        if res and maxRange[1]-maxRange[0]<(res[-1]-res[0]):
            maxRange = [res[0],res[-1]]
        print(res)
        print(maxRange)

    #s = "leet"
    #print(list(s))
    #s = list(s)
    #print(''.join(s))
