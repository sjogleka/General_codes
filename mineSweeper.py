def dfs(field,x,y,visited):
    count  =0
    print("-------- dfs ----------")
    if 0 <= x + 1 < len(field) and field[x+1][y] and [x+1,y] not in visited:
        print(x+1,y)
        count +=1
    if 0 <= x - 1 < len(field) and field[x-1][y] and [x-1,y] not in visited:
        print(x - 1, y)
        count += 1
    if 0 <= y + 1 < len(field[0]) and field[x][y+1] and [x,y+1] not in visited:
        print(x, y+1)
        count += 1
    if 0 <= y - 1 < len(field[0]) and field[x][y-1] and [x,y-1] not in visited:
        print(x , y-1)
        count += 1

    if 0<=x-1<len(field) and 0<=y-1<len(field) and field[x-1][y-1] and [x-1,y-1] not in visited:
        print(x - 1, y-1)
        count+=1
    if 0<=x+1<len(field) and 0<=y-1<len(field) and field[x+1][y-1] and [x+1,y-1] not in visited:
        print(x + 1, y-1)
        count+=1
    if 0<=x-1<len(field) and 0<=y+1<len(field) and field[x-1][y+1] and [x-1,y+1] not in visited:
        print(x - 1, y+1)
        count+=1
    if 0<=x+1<len(field) and 0<=y+1<len(field) and field[x+1][y+1] and [x+1,y+1] not in visited:
        print(x + 1, y+1)
        count+=1

    print(count)
    return count

def dfs1(field,x,y,visited):
    count  =0
    row = [1, -1, 0, 0, -1, 1, -1, 1]
    col = [0, 0, 1, -1, -1, -1, 1, 1]
    for i in range(8):
        #print("-------- dfs ----------")
        if 0<=x+row[i]<len(field) and 0<=y+col[i]<len(field[0])and field[x+row[i]][y+col[i]] and [x+row[i],y+col[i]] not in visited:
            count+=1
    #print(count)
    return count


def minsweeper(field, x,y):
    q = []
    visited = []
    row = [1,-1,0,0,-1,1,-1,1]
    col = [0,0,1,-1,-1,-1,1,1]
    if field[x][y]:
        #print("in if")
        return [[-1]*len(field[0])]*len(field)
    else:
        #print("in else")
        q.append([x,y])
        while q:
            data = q.pop(0)
            cnt = dfs1(field,data[0],data[1],visited)
            visited.append(data)
            field[data[0]][data[1]] =cnt
            if cnt == 0:
                for i in range(8):
                    if 0 <= data[0] + row[i]<len(field) and 0<=data[1]+col[i]<len(field[0])and [data[0] + row[i], data[1]+col[i]] not in visited and [data[0] + row[i], data[1]+col[i]] not in q:
                        q.append([data[0]+row[i],data[1]+col[i]])
    #print(field)

    for i in range(len(field)):
        for j in range(len(field[0])):
            if type(field[i][j]) == bool:
                field[i][j] = -1

    return field




if __name__ == '__main__':
    #field = [[False,True,True],[True,False,True],[False,False,True]]
    field = [[True, False, True,True,False], [True, False, False, False, False], [False, False, False, False, False],[True,False,False,False,False]]
    #field = [[True, False, False, False, False,True],[True, False, False, False, False,False],[True, True, False, False, False,False],[False, False, True, False, False,False],[False, False, True, True, True, True]]
    #x = 1
    #y =1
    x= 3
    y = 2
    #x =0
    #y = 5
    print(minsweeper(field,x,y))
