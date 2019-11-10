def reverseStr(s):
    num = str(s)
    i =0
    res =""
    if len(num) % 2 == 0:
        while i < len(num):
            res += num[i+1]+num[i]
            i=i+2
    else:
        while i < len(num)-1:
            res += num[i+1]+num[i]
            i=i+2
        res+=num[len(num)-1]
    return int(res)


print(reverseStr(1122558898))
print(reverseStr(1123))
print(reverseStr(12345))
print(reverseStr(72328))