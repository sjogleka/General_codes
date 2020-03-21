def ans(grid,k,rules):
    corners = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[-1,-1],[1,-1],[-1,1]]
    lc = [[0]*len(grid[0])]*len(grid)
    for l in range(k):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                count = 0
                for f in range(8):
                    r = i
                    c = j
                    r += corners[f][0]
                    c += corners[f][1]
                    if r >= 0 and r < len(grid) and c >= 0 and c<len(grid[0]) and grid[r][c] == 1:
                        count += 1
                lc[i][j] = count
        #print("lc---",lc)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if rules[lc[i][j]] == 'alive':
                    #print(rules[lc[i][j]])
                    grid[i][j] = 1
                else:
                    grid[i][j] = 0
        print("Grid",k,grid)
    return grid


def calcualte_live_cell(grid,k,rules):
    X = [-1,-1,-1,0,0,1,1,1]
    Y = [-1,0,1,-1,1,-1,0,1]

    alive= []
    for i in range(len(grid)):
        temp =[]
        for j in range(len(grid[0])):
            num_alive = 0
            for k in range(8):
                x= i+X[k]
                y = j+Y[k]

                if x>=0 and x<len(grid) and y>=0 and y< len(grid[0]) and grid[x][y]:
                    num_alive+=1
            temp.append(num_alive)

        alive.append(temp)

    for i in range(len(alive)):
        for j in range(len(alive[0])):
            if rules[alive[i][j]]:
                grid[i][j]=1
            else:
                grid[i][j] = 0

    #print(alive)
    print(grid)



#grid = [[0,1,0,0],[0,0,0,0]]
#grid = [[0,1,0,0],[0,0,0,0]]
grid = [[0,1,0,0],[0,0,0,0]]
k = 1
rules = ['dead','alive','dead','dead','dead','dead','dead','dead','dead']
#rules = ['dead','alive','dead','dead','dead','alive','dead','dead','dead']
print(ans(grid,k,rules))

calcualte_live_cell(grid,k,rules)