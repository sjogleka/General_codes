import  math
def goodSegment(badNumber, lower, upper):
    badNumber = sorted(badNumber)
    temp = []
    #print("Sorted List",badNumber)
    for i in range(len(badNumber)):
        if lower<=badNumber[i]<=upper:
            temp.append(badNumber[i])
    #maxdiff = -math.inf
    maxdiff = temp[0]-1 - lower
    if upper - temp[-1]>maxdiff:
        maxdiff = upper - temp[-1]
    #print("Res before for",maxdiff)

    for i in range(1,len(temp)):
        if maxdiff< (temp[i] - temp[i - 1])-1:
            maxdiff = (temp[i] - temp[i - 1])-1
        #print(maxdiff)

    #print(maxdiff)
    return  maxdiff

if __name__ == '__main__':
    print(goodSegment([37,7,22,15,49,60],3,48))
    print(goodSegment([5,4,2,15], 1, 10))
    print(goodSegment([8,6,20,12], 1, 30))
    print(goodSegment([2], 1, 3))