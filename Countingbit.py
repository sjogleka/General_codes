def  countSetBits(n):
    res = []
    x = (bin(n).replace("0b",""))
    print(x)
    res.append(x.count('1'))
    for i in range(0,len(x)):
        if x[i] == '1':
            res.append(i+1)
    return res


def decimalToBinary(n):
   count = 0
   s = bin(n)
   res = [s.count('1')]
   for i in range(len(s)):
      if s[i] == '1':
         res.append(i-1)
   return res

print(countSetBits(37))
print(decimalToBinary(37))