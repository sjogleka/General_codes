import  math
import heapq
if __name__ == '__main__':
    #arr = [[5,4,5],[1,2,6],[7,4,6]]
    #arr = [[3,4,6,3,4],[0,2,1,1,7],[8,8,3,2,7],[3,2,4,9,8],[4,1,2,0,0],[4,6,5,4,3]]
    #arr = [[2, 2, 1, 2, 2, 2], [1, 2, 2, 2, 1, 2]]
    arr = [[2, 0, 5, 2, 0], [2, 4, 4, 4, 3], [1, 5, 0, 0, 0], [5, 4, 4, 3, 1], [1, 3, 1, 5, 3]]
    q = [(-arr[0][0],0,0)]
    total = math.inf
    visited = set()
    while q:
        val, i ,j = heapq.heappop(q)
        visited.add((i,j))
        if -val<total:
            total = -val
        x = [1, -1, 0, 0]
        y = [0, 0, 1, -1]
        if i ==len(arr)-1 and j == len(arr[0])-1:
            break
        for ele in range(4):
            if 0 <= i + x[ele] < len(arr) and 0 <= j + y[ele] < len(arr[0]) and (i + x[ele], j + y[ele]) not in visited:
                heapq.heappush(q,(-arr[i + x[ele]][j + y[ele]],i + x[ele],j + y[ele]))


    print(total)
    print(visited)









    '''
    arr = [[2, 0, 5, 2, 0], [2, 4, 4, 4, 3], [1, 5, 0, 0, 0], [5, 4, 4, 3, 1], [1, 3, 1, 5, 3]]
    total = []
    path = [[0,0]]
    q = [[0,0]]
    while q:
        data = q.pop(0)
        #print(data)
        i = data[0]
        j = data[1]
        if i==len(arr)-1 and j== len(arr[0])-1:
            break
        if [i,j] in path:
            print("----",i,j,"-----")
            maxNum = -math.inf
            maxNumCord = (0, 0)
            num = arr[i][j]
            x = [1,-1,0,0]
            y = [0,0,1,-1]
            for ele in range(4):
                if 0<=i+x[ele]<len(arr) and 0<=j+y[ele]<len(arr[0]) and [i+x[ele],j+y[ele]] not in path:
                    print(i + x[ele],j+y[ele])
                    if [i + x[ele],j+y[ele]] ==[len(arr)-1,len(arr[0])-1]:
                        maxNum = arr[i + x[ele]][j + y[ele]]
                        maxNumCord = [i + x[ele], j + y[ele]]
                        break
                    if arr[i+x[ele]][j+y[ele]] > maxNum:
                        maxNum = arr[i + x[ele]][j+y[ele]]
                        maxNumCord = [i + x[ele], j+y[ele]]
        print(maxNumCord,maxNum)
        if maxNumCord not in path:
            path.append(maxNumCord)
            q.append(maxNumCord)
            total.append(maxNum)

    print(path)
    print(min(total))
    print(len(path)-1)

    if i+1<len(arr) and arr[i+1][j]>maxNum and [i+1,j] not in path:
        maxNum = arr[i+1][j]
        maxNumCord = [i+1,j]
    if i-1>=0 and arr[i-1][j] > maxNum  and [i-1,j] not in path:
        maxNum = arr[i - 1][j]
        maxNumCord = [i-1,j]
    if j+1<len(arr[0]) and arr[i][j+1]>maxNum and [i,j+1] not in path:
        print(arr[i][j+1])
        maxNum = arr[i][j+1]
        maxNumCord = [i,j+1]
    if j-1>=0 and arr[i][j-1]>maxNum  and [i,j-1] not in path:
        maxNum = arr[i][j-1]
        maxNumCord = [i,j-1]

'''