import sys

def sortArray(a,b):
    c = set()
    i,j = 0,0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.add(a[i])
            i+=1
        else:
            c.add(b[j])
            j+=1
    while i < len(a):
        c.add(a[i])
        i+=1
    while j < len(b):
        c.add(b[j])
        j+=1
    return list(c)

def maxArithmeticLength(a,b):
    c = sortArray(a,b)
    minDiff = sys.maxsize
    maxDiff = -sys.maxsize
    for i in range(len(c)-1):
        if minDiff > c[i+1] - c[i]:
            minDiff = c[i+1] - c[i]
        if maxDiff < c[i+1] - c[i]:
            maxDiff = c[i+1] - c[i]
    result = -1
    setA = set(a)
    while minDiff <= maxDiff:
        temp = set()
        count = 1
        j = 0
        i = c[j]
        temp.add(i)
        while j < len(c):
            i += minDiff
            if i in c:
                count += 1
                temp.add(i)
            else:
                break
            j+=1
        minDiff += 1
        if setA.issubset(temp):
            if result < count:
                result = count
    return result

print(maxArithmeticLength([0,4,8,16],[0,2,6,12,14,20]))
print(maxArithmeticLength([4,8,16],[0,2,6,10,12,14,20]))