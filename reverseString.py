def reverseString1(x):
    res=""
    for i in x:
        res = i+res

    print(res)

def reverseString2(x):
    res =[]
    finalOP=[]
    for i in x:
        res.append(i)
    while res:
        finalOP.append(res.pop())

    print(''.join(finalOP))


def reverseString3(x):
    print(x[::-1])


if __name__ == '__main__':
    s = "EAITechnology"
    reverseString1(s)
    reverseString2(s)
    reverseString3(s)
    #reverseString1("")