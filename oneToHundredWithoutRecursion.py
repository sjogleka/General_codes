def printNumbers(num):
    res = []
    def helper(i):
        if i==num:
            res.append(i)
        else:
            res.append(i)
            helper(i+1)

    helper(1)
    return res

n = 100
print(printNumbers(n))



