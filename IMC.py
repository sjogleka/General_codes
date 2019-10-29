'''
theDict = {chr(y): y - 64 for y in range(65, 91)}
print(theDict)
a = "1B 2C, 2D 4D"
x = a.split(',')
newlist = []
for i in (0, len(x) - 1):
    y = x[i].split()
    for i in range(0, len(y)):
        z = list(y[i])
        z[0] = int(z[0])
        z[1] = theDict[z[1]]
        z = ','.join(map(str, z))
        newlist.append(z)
for i in range(len(newlist)):
    newlist[i] = eval(newlist[i])

print(newlist)
for i in range(0, len(newlist), 2):
    temp = newlist[i] + newlist[i + 1]
    print(temp)
    maxnum = max(temp)
    minnum = min(temp)
    print(maxnum, minnum)
    '''


import string
import copy
def artifact(N, artifacts, search):
    # 4 , "1B 2C, 2D 4D" , "2B 2D 3D 4D 4A"

    mapOfArtifact = {}
    artifactsString = artifacts.split(",")

    for idx, artifact in enumerate(artifactsString):

        mapOfArtifact[idx] = findAllpositions(artifact)

    tempMap = copy.deepcopy(mapOfArtifact)
    searchPos = search.split()
    countOfPartial = 0
    countOfFull = 0

    for each in searchPos:
        for artifact in mapOfArtifact:
            if each in mapOfArtifact[artifact]:
                mapOfArtifact[artifact].remove(each)
    for idx,element in mapOfArtifact.items():
        if len(element) == 0:
            countOfFull += 1
        elif len(element) < len(tempMap[idx]):
            countOfPartial += 1

    print(countOfFull)
    print(countOfPartial)

def findAllpositions(s):
    a = dict()
    n = 4
    j = 65
    for i in range(n):
        a[chr(j)] = i + 1
        j += 1

    t = s.split()[0]
    b = s.split()[1]
    matrix = [[0] * n]*n
    bDict = dict()
    k = 65
    for i in range(n):
        bDict[i + 1] = chr(k)
        k += 1

    temp = []

    for i in range(int(t[0]), int(b[0]) + 1):
        for j in range(a[t[1]] -1, a[b[1]]):
            temp.append(str(i) + str(bDict[j+1]))

    return temp

findAllpositions("2D 4D")
#artifact(4, "1B 2C,2D 4D" , "2B 2D 3D 4D 4A")
artifact(4, "1A 1B,2C 2C" , "1B")