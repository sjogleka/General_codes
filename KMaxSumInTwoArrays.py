import heapq
def kMaxSumCombinations(arr1,arr2,k):
    d= {}
    for i in arr1:
        for j in arr2:
            d[i+j] = (i,j)

    items = sorted(d.keys(),reverse=True)
    #print(items)
    return items[:k]

def kMaxSumCombintion_1(arr1,arr2,k):
    arr1.sort()
    arr2.sort()
    #print(arr1,arr2)
    maxComb = []
    visited = set()
    heapq.heappush(maxComb,(-(arr1[len(arr1)-1]+arr2[len(arr2)-1]),len(arr1)-1,len(arr2)-1))
    #print(maxComb)
    res = []
    visited.add((len(arr1)-1,len(arr2)-1))
    for i in range(k):
        #print(maxComb)
        temp = heapq.heappop(maxComb)
        res.append(-temp[0])
        id1,id2 = temp[1],temp[2]
        if (id1-1,id2) not in visited:
            visited.add((id1-1,id2))
            tempsum1 = arr1[id1 - 1] + arr2[id2]
            heapq.heappush(maxComb, (-tempsum1, id1 - 1, id2))
        if (id1, id2-2) not in visited:
            visited.add((id1, id2-2))
            tempsum2 = arr1[id1] + arr2[id2 - 1]
            heapq.heappush(maxComb, (-tempsum2, id1, id2-1))
    print(res)




if __name__ == '__main__':
    #print(kMaxSumCombinations([3,2],[1,4],2))
    #print(kMaxSumCombinations([4, 2, 5, 1],[8, 0, 3, 5], 3))

    #print(kMaxSumCombintion_1([3, 2], [1, 4], 2))
    print(kMaxSumCombintion_1([4, 2, 5, 1],[8, 0, 3, 5], 3))
