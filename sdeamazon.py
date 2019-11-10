def leftrotate(string,amount):
    s = list(string)
    amount = amount%len(s)
    s = s[amount:]+s[:amount]
    return  s

def rightrotate(string,amount):
    amount = amount%len(string)
    return  leftrotate(string,len(string)-amount)

def rotatestring(originalstring,direction,amount):
    s = originalstring
    for i in range(len(direction)):
        if direction[i] ==0:
            s = leftrotate(s,amount[i])
        else:
            s = rightrotate(s,amount[i])

    return ''.join(s)


#if __name__ == '__main__':



'''
s = "rthura"

print("-------",s.copy())   
s = list(s)
print(len(s))
a = s[5:] + s[:5]
print(a)

#print("",s.copy())



s = "rthura"
s = list(s)
a = s[5:] + s[:5]
print(a)
'''