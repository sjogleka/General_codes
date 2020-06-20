'''
def getSum(BITree, index):
    sum = 0
    while (index > 0):
        sum += BITree[index]
        index -= index & (-index)

    return sum

def updateBIT(BITree, n, index, val):
    while (index <= n):
        BITree[index] += val
        index += index & (-index)

def convert(arr, n):
    temp = [0] * n
    for i in range(n):
        temp[i] = arr[i]
    temp = sorted(temp)
    j = 1
    for i in temp:
        arr[arr.index(i)] = j
        j += 1
def getInvCount(arr, n):
    convert(arr, n)
    greater1 = [0] * n
    smaller1 = [0] * n
    for i in range(n):
        greater1[i], smaller1[i] = 0, 0

    BIT = [0] * (n + 1)
    for i in range(1, n + 1):
        BIT[i] = 0
    for i in range(n - 1, -1, -1):
        smaller1[i] = getSum(BIT, arr[i] - 1)
        updateBIT(BIT, n, arr[i], 1)
    for i in range(1, n + 1):
        BIT[i] = 0
    for i in range(n):
        greater1[i] = i - getSum(BIT, arr[i])
        updateBIT(BIT, n, arr[i], 1)
    invcount = 0
    for i in range(n):
        invcount += smaller1[i] * greater1[i]

    return invcount

if __name__ == "__main__":
    #arr = [5, 3, 4, 2, 1]
    #n = 5

    arr = [4,2,2,1]
    n = 4

    print("Inversion Count : ",
          getInvCount(arr, n))
'''

def maxInversions(prices):
    n = len(prices)
    total = 0
    for i in range(1, n - 1):
        left,right = 0,0
        for j in range(i + 1, n):
            if prices[i] > prices[j]:
                left += 1
        for j in range(i - 1, -1, -1):
            if prices[i] < prices[j]:
                right += 1
        total += right * left

    return total

arr = [4, 2, 2, 1]
arr = [15,10,1,7,8]
arr = [4,1,3,2,5]
print("Inversion Count :", maxInversions(arr))
