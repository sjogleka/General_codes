def numberOfIslands(x, y):
    global count
    if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]) or matrix[x][y] != 1:
        return 0
    matrix[x][y] = '0'
    count += 1
    print(count)
    numberOfIslands(x + 1, y)
    numberOfIslands(x - 1, y)
    numberOfIslands(x, y + 1)
    numberOfIslands(x, y - 1)
    numberOfIslands(x - 1, y - 1)
    numberOfIslands(x + 1, y - 1)
    numberOfIslands(x - 1, y + 1)
    numberOfIslands(x + 1, y + 1)

    return count


if __name__ == '__main__':
    matrix = [[1,0,0,1,0],[1,0,1,0,0],[0,0,1,0,1],[1,0,1,0,1]]
    res = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] ==1:
                count = 0
                print(i,j)
                res.append(numberOfIslands(i,j))
                print(count)
    print(sorted(res))