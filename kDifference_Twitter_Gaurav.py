def kDifference(nums, k):
    if k < 0: return 0
    numsSet, pairsSet = set(), set()
    for num1 in nums:
        for num2 in [num1 + k, num1 - k]:
            if num2 in numsSet:
                pairsSet.add(tuple(sorted([num1, num2])))
        numsSet.add(num1)
    return len(pairsSet)


# Driver function to test above function
#nums = [1,5,3,4,2]
nums = [1,5,3,4,2]
#nums = [363374326,364147539,61825163,107306571,1281246024,139946991,428047635,491595254,879792181,106926279]
k= 2
print(kDifference(nums, k))