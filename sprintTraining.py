import  operator
def getMostVisited(n,sprints):
    d = {}
    minvalue = float('inf')
    for i in range(len(sprints)-1):
        if sprints[i+1]<sprints[i]:
            flag,final = True,sprints[i + 1] - 1
        else:
            flag,final = False,sprints[i + 1] + 1
        j = sprints[i]
        while j!=final:
            if j not in d:
                d[j] = 0
            d[j] += 1
            if flag:j-=1
            else:j+=1

    maxVal = max(d.items(), key=lambda x: x[1])

    for k,v in d.items():
        if v == maxVal[1] and k<minvalue:
            minvalue = k
    return minvalue


def getMostVisited_1(n,sprints):
    incremental = [0]*(n+2)
    for i in range(len(sprints)-1):
        start = min(sprints[i],sprints[i+1])
        end = max(sprints[i], sprints[i + 1])
        incremental[start]+=1
        incremental[end+1] -= 1
    scores = [0]*(n+1)
    score = 0
    for i in range(n+1):
        score+=incremental[i]
        scores[i] = score
    maxVal = max(scores)
    for i in range(1,n+1):
        if scores[i]==maxVal:   
            return i






if __name__ == '__main__':

    print(getMostVisited(5,[2,4,1,3]))
    print(getMostVisited(10, [1, 5, 10, 3]))
    print(getMostVisited(5, [1,5]))
    print(getMostVisited(9, [9,7,3,1]))

    print(".........")
    print(getMostVisited_1(5,[2,4,1,3]))
    print(getMostVisited_1(10, [1, 5, 10, 3]))
    print(getMostVisited_1(5, [1,5]))
    print(getMostVisited_1(9, [9,7,3,1]))