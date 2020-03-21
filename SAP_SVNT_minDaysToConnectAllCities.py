from collections import deque
import math

def bfs(grid, start,goal):
    queue = deque([[start]])
    seen = set([start])
    while queue:
        path = queue.popleft()
        x, y= path[-1]
        if (x,y) == goal:
            return path
        for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
            if 0 <= x2 < len(grid[0]) and 0 <= y2 < len(grid) and grid[x2][y2] != '#' and (x2, y2) not in seen:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))

def minDays(grid,visited,output):
    src=deque()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '$':
                pos = [i, j, 0]
                src.appendleft(pos)
    #print(src)
    while len(src)>0:
        curr = src.pop()
        x,y,dist= curr[0],curr[1],curr[2]
        if x+1<len(grid)and visited[x+1][y] == False  and grid[x+1][y]!='#':
            output[x+1][y] = min(output[x+1][y],dist+1)
            src.appendleft((x+1,y,dist+1))
            visited[x+1][y] = True

        if x-1>=0 and visited[x-1][y] == False and grid[x-1][y]!='#':
            output[x - 1][y] = min(output[x-1][y], dist+ 1)
            src.appendleft((x-1,y,dist+1))
            visited[x-1][y] = True

        if y+1<len(grid[0]) and visited[x][y+1] == False and grid[x][y+1]!='#':
            output[x][y+1] = min(output[x][y+1],dist + 1)
            src.appendleft((x,y+1,dist+1))
            visited[x][y+1] = True

        if y-1>=0 and visited[x][y-1] == False  and grid[x][y-1]!='#':
            output[x][y-1] = min(output[x][y-1],dist + 1)
            src.appendleft((x,y-1,dist+1))
            visited[x][y-1] = True


if __name__ == '__main__':
    #g = [['$', '.', '.', '#'],['.', '.', '#', '.'],['#', '.', '$', '.'],['$', '.', '.', '.']]
    g = [['$', '.', '.', '#'],['.', '.', '#', '.'],['#', '.', '$', '.'],['.', '.', '.', '.']]
    #g = [['$','#'],['$','.']]
    visited = [[False for i in range(len(g))] for i in range(len(g[0]))]
    output = [[-1 for i in range(len(g))] for i in range(len(g[0]))]
    src= []
    p = {}
    for i in range(len(g)):
        for j in range(len(g[0])):
            if g[i][j] == '$':
                src.append([(i,j),math.inf])
    for i in range(len(src)):
        for j in range(i+1,len(src)):
            temp = bfs(g,src[i][0],src[j][0])
            if len(temp)<src[i][1]:
                src[i][1] = len(temp)
                p[src[i][0]] = temp
                p[src[j][0]] = temp
    for k,v in p.items():
        for j in range(len(v)):
            output[v[j][0]][v[j][1]] = max(output[v[j][0]][v[j][1]],j)
            visited[v[j][0]][v[j][1]] = True
    print(output)
    for i in range(len(output)):
        for j in range(len(output[0])):
            if output[i][j] == -1:
                output[i][j] = math.inf

    print(visited)
    minDays(g, visited,output)
    total = 0
    for i in range(len(output)):
        for j in range(len(output)):
            if output[i][j] !=math.inf:
                total+=output[i][j]

    print(total)








