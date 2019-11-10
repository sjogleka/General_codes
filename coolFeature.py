def pairwithSum(x,y,n):
    count = 0
    for k in range(len(x)):
        for j in range(len(y)):
            if x[k] + y[j] == n:
                count += 1
    #print(count)
    return count

def pairwithSum1(x,y,q):
    m ={}
    result = []
    for i in range(len(x)):
        if x[i] not in m:
            m[x[i]] =1
        else:
            m[x[i]] +=1
    for i in range(0,len(q)):
        if len(q[i]) == 3:
            index = q[i][1]

            y[index] = q[i][2]
        if len(q[i])==2:
            sum = q[i][1]
            count = 0
            for j in range(0,len(y)):
                if sum - y[j] in m:
                    count+=m[sum -y[j]]
            result.append(count)

    return  result

x = [1,2,3]
#x = [1,2,2]
y = [3,4]
#y = [2,3]
q = [[1,5],[0,0,1],[1,5]]
#q = [[1,4],[0,0,3],[1,5]]

print(pairwithSum1(x,y,q))

def coolFeature(a,b,query):
    m=[]
    if len(a) or len(b) == 0:
        return []
    for i in range(len(query)):
        count=0
        if query[i][0] == 0:
            if query[i][1]<len(query[i][1]):
                b[query[i][1]] = query[i][2]
        else:
            for k in range(len(a)):
                for j in range(len(b)):
                    if a[k] + b[j] == query[i][1]:
                        count+=1
            m.append(count)
    return m

'''
res = []
for i in range(len(q)):
    if len(q[i])==2:
        #print(pairwithSum(x,y,q[i][1]))
        res.append(pairwithSum(x,y,q[i][1]))
    elif len(q[i])==3:
        temp = q[i]
        y.pop(temp[1])
        y.insert(temp[1],temp[2])
print(res)
'''
#print(coolFeature(x,y,q))
#print(coolFeature(x,y,q))
