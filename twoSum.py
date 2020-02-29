a = [2,7,11,15]
target = 9
d ={}
for i in range(len(a)):
    if a[i] not in d:
        d[target - a[i]] = i
    else:
        print([d[a[i]],i])


