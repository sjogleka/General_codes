def uniquePath(m,n):
    grid = [[1 for i in range(m)] for j in range(n)]
    for i in range(n-2,-1,-1):
        for j in range(1,m):
            grid[i][j] = grid[i][j-1]+grid[i+1][j]
    return  grid


if __name__ == '__main__':
    print(uniquePath(3,2))
    print(uniquePath(7, 3))