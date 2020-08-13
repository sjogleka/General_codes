def numberOfIncreasingPaths(matrix):

    dp = [[0 for _ in range(len(matrix[0]))]for _ in range(len(matrix))]
    s = set()
    for i in range(1,len(matrix)):
        if matrix[i][0]>matrix[i-1][0]:
            s.add((i,0,i-1,0))
            dp[i][0] += dp[i-1][0]+1
        if matrix[i][0]<matrix[i-1][0]:
            s.add((i-1, 0, i, 0))
            dp[i][0] += dp[i-1][0]+1

    print(dp)
    for j in range(1, len(matrix[0])):
        if matrix[0][j] > matrix[0][j-1]:
            s.add((0, j, 0, j-1))
            dp[0][j] += dp[0][j-1] + 1
        if matrix[0][j] < matrix[0][j-1]:
            s.add((0, j-1, 0, j))
            dp[0][j] += dp[0][j-1] + 1

    print(dp)

    for i in range(1,len(matrix)):
        for j in range(1,len(matrix[0])):
            if matrix[i][j]>matrix[i-1][j] and (i,j,i-1,j) not in s:
                s.add((i,j,i-1,j))
                dp[i][j] +=dp[i-1][j]+1
            print("...",dp)
            if matrix[i][j]>matrix[i][j-1] and (i,j,i,j-1) not in s:
                s.add((i,j,i,j-1))
                dp[i][j] += dp[i][j-1]+1
    print(dp)
    for i in range(1,len(matrix)):
        for j in range(len(matrix[0])-1,0,-1):
            print(i,j)
            if matrix[i][j]>matrix[i-1][j] and (i,j,i-1,j) not in s:
                s.add((i,j,i-1,j))
                dp[i][j] += dp[i-1][j]+1
            if matrix[i][j]>matrix[i][j-1] and (i,j,i,j-1) not in s:
                s.add((i,j,i,j-1))
                dp[i][j] += dp[i][j-1]+1
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            count+=dp[i][j]
    print(dp)
    print(count)
    return count
    '''
    s1 = set()
    s2 = set()
    dp = [[[0,0] for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    for i in range(1, len(matrix)):
        if matrix[i][0] > matrix[i - 1][0]:
            s1.add((i, 0, i - 1, 0))
            dp[i][0][0] += dp[i - 1][0][0] + 1
    for i in range(len(matrix)-1,0,-1):
        if matrix[i][0] < matrix[i-1][0]:
            s2.add((i - 1, 0, i, 0))
            dp[i][0][1] += dp[i-1][0][1] + 1

    for j in range(1, len(matrix[0])):
        if matrix[0][j] > matrix[0][j - 1]:
            s1.add((0, j, 0, j - 1))
            dp[0][j][0] += dp[0][j - 1][0] + 1
    for j in range(len(matrix[0])-1,0,-1):
        if matrix[0][j] < matrix[0][j -1]:
            s2.add((0, j - 1, 0, j))
            dp[0][j][1] += dp[0][j - 1][1] + 1

    print("Dp after 1st row and index",dp)

    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if matrix[i][j] > matrix[i - 1][j] and (i, j, i - 1, j) not in s1:
                s1.add((i, j, i - 1, j))
                dp[i][j][0] += dp[i - 1][j][0] + 1
            print("...", dp)
            if matrix[i][j] > matrix[i][j - 1] and (i, j, i, j - 1) not in s1:
                s1.add((i, j, i, j - 1))
                dp[i][j][0] += dp[i][j - 1][0] + 1
    print(dp)
    for i in range(len(matrix)-2,0,-1):
        for j in range(len(matrix[0]) - 2, 0, -1):
            print(i, j)
            if matrix[i][j] < matrix[i + 1][j] and (i, j, i + 1, j) not in s2:
                s2.add((i, j, i + 1, j))
                dp[i][j][1] += dp[i + 1][j][1] + 1
            if matrix[i][j] < matrix[i][j + 1] and (i, j, i, j + 1) not in s2:
                s2.add((i, j, i, j + 1))
                dp[i][j][1] += dp[i][j + 1][1] + 1
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            count += dp[i][j][0]+ dp[i][j][1]
    print(dp)
    print(count)
    return count
'''


if __name__ == '__main__':
    #grid = [[0,4,3],[5,8,9],[5,9,9]]
    #grid = [[5,1],[2,7]]
    grid = [[0,4,3],[5,8,9],[5,9,9]]
    '''
    grid = [
    [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14],
    [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],
    [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],
    [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17],
    [4,5,6,7,8,9,10,11,12,13,14,15,16,17,18],
    [5,6,7,8,9,10,11,12,13,14,15,16,17,18,19],
    [6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
    [7,8,9,10,11,12,13,14,15,16,17,18,19,20,21],
    [8,9,10,11,12,13,14,15,16,17,18,19,20,21,22],
    [9,10,11,12,13,14,15,16,17,18,19,20,21,22,23],
    [10,11,12,13,14,15,16,17,18,19,20,21,22,23,24],
    [11,12,13,14,15,16,17,18,19,20,21,22,23,24,25],
    [12,13,14,15,16,17,18,19,20,21,22,23,24,25,26],
    [13,14,15,16,17,18,19,20,21,22,23,24,25,26,27],
    [14,15,16,17,18,19,20,21,22,23,24,25,26,27,28]]
    '''
    print(numberOfIncreasingPaths(grid))