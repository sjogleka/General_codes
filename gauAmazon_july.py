import math, heapq

def find(totalCratesm, num,truckCapacity):
    arr,res = [],[]
    allocate = []
    for i in range(len(num)):
        if num[i] not in allocate:
            allocate.append(num[i])

    for i in range(len(allocate)):
        heapq.heappush(arr, ((allocate[i][1] ** 2 + allocate[i][0] ** 2), allocate[i]))
    while truckCapacity and len(arr)!=0:
        res.append(heapq.heappop(arr)[1])
        truckCapacity-=1
    return res if len(res)!=0 else [[]] #change


import random

def kClosest(s,allocations,K):
    #num = list(set(tuple(x) for x in allocations))
    num = []
    for i in range(len(allocations)):
        if allocations[i] not in num:
            num.append(allocations[i])

    dist = lambda i: num[i][0] * 2 + num[i][1] * 2

    def sort(i, j, K):
        if i >= j: return
        k = random.randint(i, j)
        num[i], num[k] = num[k], num[i]

        mid = partition(i, j)
        if K < mid - i + 1:
            sort(i, mid - 1, K)
        elif K > mid - i + 1:
            sort(mid + 1, j, K - (mid - i + 1))

    def partition(i, j):
        oi = i
        pivot = dist(i)
        i += 1
        while True:
            while i < j and dist(i) < pivot:
                i += 1
            while i <= j and dist(j) >= pivot:
                j -= 1
            if i >= j: break
            num[i], num[j] = num[j], num[i]

            num[oi], num[j] = num[j], num[oi]
        return j

    sort(0, len(num) - 1, K)
    return num[:K] if len(num)!=0 else [[]]

if __name__ == '__main__':
    a = [[1,2],[3,4],[1,-1],[1,-1],[1,-1],[1,-1]]
    #a = [[1,-3],[1,2],[3,4]]
    #a = [[3, 6], [2, 4], [5, 3],[2,7],[1,8],[7,9]]

    print(find(3,a,1))
    print(kClosest(0,[], 0))
    #print(find(6, a, 3))





