def getMaximumscore(integerArray,start,end, operation, sum1,score):
    if sum1 ==0:
        return score
    if operation%2 ==0:
        score -=sum1
    else:
        score +=sum1
    score1 = getMaximumscore(integerArray,start+1,end,operation+1,sum1-integerArray[start],score)
    score2 = getMaximumscore(integerArray,start,end-1,operation+1,sum1-integerArray[end],score)
    return max(score1,score2)

if __name__ == '__main__':
    #n = 6
    #n =3
    n = 1
    #integerArray = [1, 2, 3, 4, 2, 6]
    #integerArray = [1,2,3 ]
    integerArray = [10]
    initialScore = 0
    print(getMaximumscore(integerArray,0,len(integerArray)-1,1,sum(integerArray),0))
