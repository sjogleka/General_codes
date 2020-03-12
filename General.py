def findFirst1(arr,tatget):
    def helper(start,end,target):
        mid = (start+end)//2
        if end>=start:
            if arr[mid]==target and arr[mid-1]!=target:
                return mid
            elif arr[mid]>=target:
                return helper(start,mid-1,tatget)
            elif arr[mid]<tatget:
                return helper(mid+1,end,tatget)
        else:
            return -1
    print(helper(0,len(arr),tatget))


def findFisrtANdLast(arr,target):
    def helper(lo,hi,left):
        found = -1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if target > arr[mid]:
                lo = mid + 1
            elif target < arr[mid]:
                hi = mid - 1
            else:
                if left:
                    found = mid
                    hi = mid - 1
                else:
                    found=mid
                    lo = mid+1

        return found

    l = helper(0,len(arr)-1,True)
    r = helper(0,len(arr)-1,False)

    print(l,r)



if __name__ == '__main__':
    #findFirst1([0, 0, 0, 0, 0, 0, 1, 1, 1, 1],1)

    findFisrtANdLast([5,7,7,8,8,10],8)
    findFisrtANdLast([5, 7, 7, 8, 8, 10,10,10,10,10,11,13,15], 10)
    findFisrtANdLast([5, 7, 7, 8, 8, 10, 10, 10, 10, 11, 13, 15], 16)
    findFisrtANdLast([5,7,7,8,8,10], 6)


