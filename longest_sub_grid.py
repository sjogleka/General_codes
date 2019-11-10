def matrxi1(a,maxSum):
    n = len(a)
    for i in range(n-1,-1,-1):
        for j in range(0,n-i):
            for k in range(0,n-i):
                sum = 0
                for l in range(j,j+i):
                    for m in range(k,k+i):
                        print(l,m)
                        sum+= a[l][m]
                if (sum <= maxSum):
                    return (i)
    return 0


def matrxi(a, maxSum):
    n = len(a)
    for i in range(n, 0, -1):
        flag = 0
        for j in range(0, n - i + 1):
            if (j == 0 or flag == 1):
                flagk = 0
                for k in range(0, n - i + 1):
                    if (k == 0 or flagk == 1):
                        sum = 0
                        for l in range(j, j + i):
                            for m in range(k, k + i):
                                sum += a[l][m]
                        if (sum <= maxSum):
                            flagk = 1
                            flag = 1
                        else:
                            flag = 0
                            flagk = 0
            else:
                break
        if j == n - i and flag == 1:
            return i

    return 0


#print(matrxi([[1,1,1],[1,1,1],[1,1,1]],4))
#print(matrxi([[1,1,1],[1,1,1],[1,1,1]],4))

print(prblm_11())