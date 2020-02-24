def countWays(arr, n):
    pos = [0 for i in range(n)]
    p = 0
    for i in range(n):
        if (arr[i] == 1):
            pos[p] = i + 1
            p += 1
    if (p == 0):
        return 0
    ways = 1
    for i in range(p - 1):
        ways *= pos[i + 1] - pos[i]
    return ways

print(countWays([0,1],2))