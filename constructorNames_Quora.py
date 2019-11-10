def constructorNames(a, b):
    if len(a) != len(b):
        return False
    myA = {}
    myB = {}
    for i in range(len(a)):
        if a[i] not in b or b[i] not in a:
            return False
        if a[i] not in myA:
            myA[a[i]] = 1
        else:
            myA[a[i]] += 1
        if b[i] not in myB:
            myB[b[i]] = 1
        else:
            myB[b[i]] += 1
    for ka, va in myA.items():
        for kb, vb in list(myB.items()):
            if va == vb:
                myB.pop(kb)
    if len(myB) == 0:
        return True
    return False

print(constructorNames("babczzz","abbzccc"))
print(constructorNames("aabbzqqq","aabbzzzq"))
print(constructorNames("x","y"))