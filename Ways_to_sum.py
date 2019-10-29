'''
def binomialCoeff(n, k):
    C = [[0 for i in range(k + 1)] for i in range(n + 1)]

    # Caculate value of Binomial Coefficient in bottom up manner
    for i in range(1, n + 1, 1):
        for j in range(1, min(i, k) + 1, 1):
            # Base Cases
            if (j == 0 or j == i):
                C[i][j] = 1

            # Calculate value using previosly stored values
            else:
                C[i][j] = C[i - 1][j - 1] + C[i - 1][j]
    #print(C[n][k])
    return C[n][k]

def CountWays(n,k):
    table = [0] * (n + 1)
    table[0] = 1
    for i in range(0, k):

        for j in range(i, n+1):
            table[j] += table[j - i]

    return table[n]

# Driver Code
if __name__ == '__main__':
    n = 8
    k = 2
    print("Total number of different ways are", binomialCoeff(n - 1, k - 1))
    #print("Total number of different ways are", CountWays(8,2))


'''
def findCombinationsUtil(arr, index, num,reducedNum,main_temp):
    if (reducedNum < 0):
        return 0;
    if (reducedNum == 0):
        temp = []
        for i in range(index):
            temp.append(arr[i])
        main_temp.append(temp)
        return 0;
    prev = 1 if (index == 0) else arr[index - 1];
    for k in range(prev, num + 1):
        arr[index] = k;
        findCombinationsUtil(arr, index + 1, num,reducedNum - k,main_temp);
def findCombinations(n,a):
    arr = [0] * n
    main_temp = []
    findCombinationsUtil(arr, 0, n, n,main_temp)
    count = 0
    for array in main_temp:
        print("In for")
        if max(array) <= a:
            count += 1
    print(count)

n = 100
a=10
findCombinations(n,a)