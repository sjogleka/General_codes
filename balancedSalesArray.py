def getBalancedIndex(sales):
    sumAsc = [0] * len(sales)
    sumDesc = [0] * len(sales)
    for i in range(len(sales)):
        if i ==0:
            sumAsc[i] = sales[i]
        else:
            sumAsc[i] = sumAsc[i-1]+ sales[i]

    for i in range(len(sales)-1, -1, -1):
        if i == len(sales) -1:
            sumDesc[i] = sales[i]
        else:
            sumDesc[i] = sumDesc[i+1] + sales[i]

    for i in range(len(sales)):
        if sumAsc[i] == sumDesc[i]:
            return i
    return -1

print(getBalancedIndex([1,2,3,3]))
print(getBalancedIndex([3,1,2,1]))

