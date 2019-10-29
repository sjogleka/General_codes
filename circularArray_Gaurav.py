import operator
from collections import Counter

def prints(a, n, ind,end):
    visited = []
    b = [None] * 2 * n
    i = 0
    while i < n:
        b[i] = b[n + i] = a[i]
        i = i + 1
    i = ind
    visited.append(ind)
    while i < n + ind:
        visited.append(b[i])
        i = i + 1
        if b[i] == end:
            #print(end)
            visited.append(end)
            return visited

def prints1(a,n,start ,end):
    st= start
    visited = []
    #print(start,end)
    for i in range(0,(end-start)+1):
        if st%n ==0:
            visited.append(n)
        else:
            visited.append(st%n)
        st += 1
    return visited

def prints2(a,n,start ,end):
    st= start
    en = end
    visited = []
    print("Start",st,"End",en)
    while en < n + i :
        print(a[(i % n)], end = " ")
        i = i + 1
    return visited

def circularArray(n,endNode):
    i =0
    visitedDict = {}
    a = [item for item in range(1, n + 1)]
    #print(a)

    while i < len(endNode)-1:
        #print(a)
        visited = prints(a,n,endNode[i],endNode[i+1])
        #visitedDict.extend(visited)

        for each in visited:
            if each in visitedDict:
                visitedDict[each] += 1
            else:
                visitedDict[each] = 1
        i += 1
    #print(visitedDict)
    new  = sorted(visitedDict, key=lambda k: (-visitedDict[k], k))
    print(new)
    #occurence_count = Counter(visitedDict)
    #return max(visitedDict.items(), key=operator.itemgetter(1))[0]
    #print(occurence_count.most_common())
    return new[0]
    #return  occurence_count.most_common(1)[0][0]

#print(circularArray(5,[1,5]))
#print(circularArray(10,[1,5,10,5]))
print(circularArray(10,[1,5,10,5]))
#print(circularArray(3,[1,3,2,3]))

#start = 5
# Driver Code
'''a = [1,2,3,4,5,6,7,8,9,10]
n = 10
end = 1
print(prints(a, n, start,end))'''