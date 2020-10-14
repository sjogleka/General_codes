def calculateAmount(arr):
    if not arr:
        return 0
    finalPrice =  arr[0]
    minTillNow = arr[0]
    for i in range(len(arr)):
        if i+1<len(arr):
            finalPrice+=max(arr[i+1]-minTillNow,0)
            if arr[i+1]<minTillNow:
                minTillNow = arr[i+1]

    #print(finalPrice)
    return finalPrice


'''
            else:
                y  = min(arr[i-1],arr[i])
                finalPrice+=max(arr[i+1]-y,0)'''

calculateAmount([2,5,1,4])
calculateAmount([4,9,2,3])
calculateAmount([1,2,3,4])
calculateAmount([18,1,1,16,12,10,18,19,6,6])

