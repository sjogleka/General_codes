from collections import defaultdict
def printSumSimple(mat, k):
    n = len(mat)
    m = len(mat[1])
    if (k > n):
        return
    dic = defaultdict(list)
    for i in range(n - k + 1):
        for j in range(m - k + 1):
            l = []
            sum1 = 0
            for p in range(i, k + i):
                for q in range(j, k + j):
                    sum1 += mat[p][q]
                    l.append(mat[p][q])
            dic[sum1].extend(l)
    res = dic[max(dic.keys())]
    unique = set(res)
    print(sum(unique))







# Driver Code
if __name__ == "__main__":

    mat = [[1, 0, 1, 5, 6],
           [3, 3, 0, 3, 3],
           [2, 9, 2, 1, 2],
           [0, 2, 4, 2, 0]
           ]

    '''    mat = [[1, 1, 1, 1, 1],
               [2, 2, 2, 2, 2],
               [3, 3, 3, 3, 3],
               [4, 4, 4, 4, 4],
               [5, 5, 5, 5, 5]]
    '''

    k = 2
    printSumSimple(mat, k)