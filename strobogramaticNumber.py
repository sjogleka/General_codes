def findNotStobogrammaticNumbers(start,end):
    d = {"0":"0","1":"1","6":"9","8":"8","9":"6"}
    op  =[]
    for i in range(start,end+1):
        i = str(i)
        temp = ""
        for j in i:
            if j in d:
                temp+=d[j]
            else:
                temp=""
                break
        temp = temp[::-1]
        #print(i,temp)
        if i !=temp and len(temp)==len(i):
            op.append(i)

    print(op)





print(findNotStobogrammaticNumbers(1,100))