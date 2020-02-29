def Solution(A, K):
    n = len(A)
    best = 0
    count = 1

    for i in range(n - K - 1):
        if (A[i] == A[i + 1]):
            count = count + 1
        else:
            count = 1 # Changes
        best = max(best, count)

    result = best + K # Changes
    return result


def Solution1(A,K):
    n = len(A)
    best = 0
    count = 1
    for i in range(n-K-1):
        if (A[i]==A[i+1]):
            count = count+1
        else:
            count = 0
        best = max(best,count)
    if count == 0 and best == 1:
        result = best + K
    else:
        result = best+1+K
    return result

#A= [1,1,3,3,3,4,5,5,5,5]
#A= [1,1,3,3,3,5,6,7]
#A=[1,2]
A =[]
#A = [1,2,3,4,5]
#A = [3,3,3,4]
#A = [1,2,3,4,4,5,5,7,7]
K = 0
print(Solution(A,K))