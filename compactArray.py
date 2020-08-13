def compactArray(ip):
    if not ip:
        return ""
    i = 0
    j = 1
    res= []
    while i<len(ip):
        temp = ip[i]
        while j<len(ip) and temp+1==ip[j]:
            temp = ip[j]
            j+=1
        if i==j-1:
            res.append(str(ip[i]))
        else:
            res.append(str(ip[i])+" to "+str(ip[j-1]))
        i=j
        j+=1
    print(res)



if __name__ == '__main__':
    arr = [1,2,3,6,7,8,10,15]
    arr = [10,20,30,40]
    arr = [1,2]
    compactArray(arr)