def journey(arr, k):
    sum = 0
    length = len(arr)
    end = length
    i = 0
    max = 0
    flag = 0
    ind = -1
    while (i < length):
        if (arr[i] >= 0):
            sum += arr[i]
        else:
            temp = i + k
            max = -9999
            ind = -1
            for j in range(i, temp):
                if (j < length):
                    if (arr[j] >= 0):
                        i = j
                        sum += arr[j]
                        flag = 1
                        break;
                    else:
                        if (arr[j] > max):
                            max = arr[j]
                        ind = j
                else:
                    break
            if (flag == 0):
                sum += max
                i = ind
        i += 1
    return sum


def journey1(path, k):
    d = {}

    def helper(path, k, i):
        if i >= len(path):
            return 0
        allPresent = True
        t = [x for x in range(i + 1, i + k + 1)]
        for x in t:
            if x not in d:
                allPresent = False
        if allPresent:
            maxi = 0
            for x in t:
                if d[x] > maxi:
                    maxi = d[x]
            return maxi
        else:
            maxi = 0
            for x in t:
                temp = path[i] + helper(path, k, x)
                if temp > maxi:
                    maxi = temp
            d[i] = maxi
            return maxi

    return helper(path, k, 0)

#arr = [10,2,-10,5,20]
#arr = [10,-20,-5]
arr = [3,-4,-3,-5,0]
k = 2
print("The array is:",arr)
print("The value of the k is:",k)
print("Maximu score achievable is:",journey(arr,2))