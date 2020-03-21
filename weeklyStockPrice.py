def getWeeklyPrice(nums):
    res = []
    l,sum = 0,0

    for r in range(len(nums)):
        if r-l ==7:
            res.append(round((sum/7.0*100)/100.0,2))
            l+=1
            sum -=nums[l]

        sum+=nums[r]

    res.append(round((sum/7.0*100)/100.0,2))
    print(res)
    return "".join([str(integer) for integer in res])



if __name__ == '__main__':
    print(getWeeklyPrice([7,8,8,11,9,7,5,6]))
