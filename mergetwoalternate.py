a = "abc"
b = "defqq"
i =0
result=[]
while i<len(a) or i<len(b):
    if i<len(a):
        result.append(a[i])
    if i<len(b):
        result.append(b[i])
    i+=1
print(''.join(result))