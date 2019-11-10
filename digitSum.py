
def digitSum(n1,n2):
    d = {}
    count = 0
    print(n2+1-n1)
    n2 =n2+1
    i =n1
    while i < n2:
        if i>9:
            if i%10 !=0:
                temp = int(i%10)
            else:
                n2 = n2+1
                i+=1
                continue
        else:
            temp = i
        if temp in d:
            d[temp] +=1
        else:
            d[temp] = 1
        i+=1
    key = max(d.values())
    print("Key",key)
    for i in d.values():
        if i == key:
            count+=1
    print(d)
    return (count,get_key(d,key))


def get_key(d,val):
    for key, value in d.items():
         if val == value:
             return key

print(digitSum(3,12))
print(digitSum(1,10))
print(digitSum(1,5))

