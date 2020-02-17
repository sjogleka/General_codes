def binarySearch(array,target):
    def helper(start,end):
        mid = (start+end)//2
        if start<=end:
            if array[mid]==target and (array[mid-1]!=target):
                return mid
            elif array[mid]>=target:
                return helper(start,mid-1)
            elif array[mid]<target:
                return helper(mid+1,end)
        else:
            return -1

    return helper(0,len(array)-1)

print(binarySearch([1,1,1,1,2,2,2,4,4,4],4))