def findLoop(n,m,arr):
    for i in range(n):
        x = arr[i]
        for j in range(m):
            if arr[i+j] != x:
                break

