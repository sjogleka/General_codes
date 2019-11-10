def removeDuplicates(nums):
    i = 0
    print(nums)
    while i<len(nums)-1:
        if nums[i]==nums[i+1]:
            del nums[i]
        else:
            i+=1
    return nums


print(removeDuplicates([0,0,1,1,1,2,2,3,3,3,4]))
#print(removeDuplicates([1,1,2]))