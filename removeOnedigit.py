s = "ab12c"
#t = "1zz456"
t  = "ab24z"
def removeOneDigit(s,t):
    sList = list(s)
    tList = list(t)
    count = 0
    for i in range(len(tList)):
        tl = tList.copy()
        if tList[i].isdigit():
            tl.pop(i)
            if s < ''.join(tl):
                count+=1
    for i in range(len(sList)):
        sl = sList.copy()
        if sList[i].isdigit():
            sl.pop(i)
            if ''.join(sl) < t:
                count+=1
    return count


print(removeOneDigit(s,t))