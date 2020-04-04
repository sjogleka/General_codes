import heapq
def connectNropes(arr1):
    res =[]
    for i in range(len(arr1)):
        heapq.heappush(res,arr1[i])
    count =0
    while len(res)!=1:

        data1 = heapq.heappop(res)
        data2 = heapq.heappop(res)
        #print(data1, data2)
        count+=data1+data2
        heapq.heappush(res,data1+data2)

    print(count)

if __name__ == '__main__':
    connectNropes([4,3,2,6])