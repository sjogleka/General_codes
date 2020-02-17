a = "abc"
b = "def"
i =0
result =""
while i<len(a) or i<len(b):
    if i<len(a):
        result=result+a[i]
    if i<len(b):
        result = result + b[i]
    i+=1
print(result)
