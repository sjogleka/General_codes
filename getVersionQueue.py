def getVersion(arr,v):
    q = []
    pop = 0
    push = 0
    d = {}
    for i in range(len(arr)):
        if len(arr[i])>1:
            q.append(arr[i][1])
            push +=1
        elif len(arr[i])==1:
            pop+=1
        d[i+1] = [pop,push]

    print(q[d[v][0]:d[v][1]])


if __name__ == '__main__':
    given = [[0,1],[0,2],[1],[1],[0,3]]
    version = 5
    getVersion(given,version)
