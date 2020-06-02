def moves(arr):
    count,l,r  = 0,0,len(arr)-1
    while l<r:
        while arr[l]%2==0 and l<r:l+=1
        while arr[r]%2==1 and l<r:r-=1
        if l<r:
            arr[l],arr[r] = arr[r],arr[l]
            l+=1
            r-=1
            count+=1
    return count

print(moves([17,4,8]))
print(moves([6,3,4,5]))
print(moves([13,10,21,20]))
print(moves([8,5,11,4,6]))