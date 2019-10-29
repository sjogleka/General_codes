def romanToInt(s):
    num = 0
    my_funcs = {
        'I': (lambda num: -1 if num >= 5 else 1),
        'V': (lambda num: 5),
        'X': (lambda num: -10 if num >= 50 else 10),
        'L': (lambda num: 50),
        'C': (lambda num: -100 if num >= 500 else 100),
        'D': (lambda num: 500),
        'M': (lambda num: 1000)
    }
    for el in reversed(list(s)):
        # print(el)
        num += my_funcs[el](num)

    return num


#s = ['Louis VIII','Louis VII']
s = ['Philippe I','Philip II']
for i in range(len(s)):
    a =(s[i].split(' '))
    a[1]=str(romanToInt(a[1]))
    a = ''.join(a)
    s[i]=a


#print(s)

print(sorted(s))