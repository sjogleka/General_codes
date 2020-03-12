def findPrime(start,end):
    res =[]
    for val in range(start,end+1):
        temp = str(val)
        if int(temp[0])%2==0 or int(temp[-1])%2==0:
            continue
        if val>1:
            for n in range(2,val):
                if val%n==0:
                    break
            else:
                res.append(val)
    return res

def ifCircular(op,re):
    reverNum=0
    temp = re
    while re > 0:
        a = re % 10
        reverNum = reverNum * 10 + a
        re = re // 10
    print(reverNum,temp)
    if reverNum==temp:
        return False
    elif reverNum in op:
        return True

if __name__ == '__main__':
    op = findPrime(1,100)
    res =[]
    for i in range(len(op)):
        if ifCircular(op,op[i]):
            res.append(op[i])

    print(res)
    print(len(res))