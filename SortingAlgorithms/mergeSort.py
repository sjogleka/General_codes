def mergeSort(arr):
    #print(arr)
    if len(arr)>1:
        mid = len(arr)//2
        leftarr = arr[:mid]
        rightarr = arr[mid:]
        mergeSort(leftarr)
        mergeSort(rightarr)
        #print(leftarr,rightarr)
        i,j,k = 0,0,0
        while i<len(leftarr) and j<len(rightarr):
            if leftarr[i]<rightarr[j]:
                arr[k] = leftarr[i]
                i+=1
            else:
                arr[k] = rightarr[j]
                j+=1
            k+=1
        while i<len(leftarr):
            arr[k] = leftarr[i]
            i+=1
            k+=1
        while j<len(rightarr):
            arr[k] = rightarr[j]
            j+=1
            k+=1





if __name__ == '__main__':
    arr = [12,11,1,4,10,5]
    mergeSort(arr)
    print(arr)


