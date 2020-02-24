#temp = [10,20,10,15,5,30,20]
#temp = [18,5,15,18,11,15,9,7]
temp = [6,18,8,14,10,12,18,9]
#size = 5
size = 8
#k = 1
k = 3
res = 0
while size>0:
    arr = temp[:k]+temp[-k:]
    #print(arr)
    m = max(arr)
    if m in temp[:k]:
        temp.remove(m)
    else:
        temp.reverse()
        temp.remove(m)
        temp.reverse()
    res+=m
    print(res)
    size-=1