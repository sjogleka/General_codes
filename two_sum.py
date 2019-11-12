def twoSum(nums,target):
    nums_position = {}
    count = 0
    count_1 = 0
    for i in nums:
        if target - i in nums_position:
            count_1 +=1
        nums_position[i] = count
        count = count + 1
    return count_1


print(twoSum([10,3,5,7,2,8,9,6,1,4],7))