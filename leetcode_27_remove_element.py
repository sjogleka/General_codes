from typing import List
def removeElement(nums: List[int], val: int) -> int:
    length = len(nums)
    count = 0
    for i in range(0,length):
        #print(nums[i],val,length)
        i -=count
        if nums[i]==val:
            print("in if", nums[i])
            #nums.pop(i)
            nums.remove(nums[i])
            count +=1
    return len(nums)



if __name__ == '__main__':
    print(removeElement([0,1,2,2,3,0,4,2],2))