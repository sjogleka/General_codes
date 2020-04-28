def bfs(walker):
    if len(walker)<0:
        return "Error"
    q = []
    visited = set()
    x = [1,-1,0,0]
    y = [0,0,1,-1]
    q.append((0,0))
    while q:
        data = q.pop(0)
        visited.add(data)
        for i in range(4):
            new_x = data[0] + x[i]
            new_y = data[1] + y[i]
            #print(new_x,new_y)
            if 0<=new_x<len(walker) and 0<=new_y<len(walker) and (new_x,new_y) not in visited:
                if walker[new_x][new_y] ==1:
                    return [new_x,new_y]
                elif walker[new_x][new_y]==0:
                    q.append((new_x,new_y))

    return "No Route"



if __name__ == '__main__':
    #walker = [[0, 0, 0], [0, 0, 0], [2, 1, 1]]
    #walker = [[0, 0, 1], [2, 0, 0], [1, 2, 1]]
    walker =  [[0, 2, 1], [2, 2, 0], [1, 2, 1]]

    print(bfs(walker))
