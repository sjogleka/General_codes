def insertionSort(arr):

    for i in range(len(arr)):
        temp = arr[i]
        j = i-1
        while j>=0 and temp<arr[j]:
            arr[j+1]  = arr[j]
            j-=1

        arr[j+1] = temp

    print(arr)



if __name__ == '__main__':
    insertionSort([11,4,1,60,13,5])


'''
    for i in range(len(arr)):
        key = arr[i]
        j = i-1
        while j>=0 and key<arr[j]:
            #print(arr[j+1],j)
            arr[j+1] = arr[j]
            j-=1
        arr[j+1]  = key

    print(arr)

'''