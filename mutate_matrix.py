def rotate90Clockwise(A):
    N = len(A)
    for i in range(N // 2):
        for j in range(i, N - i - 1):
            temp = A[i][j]
            A[i][j] = A[N - 1 - j][i]
            A[N - 1 - j][i] = A[N - 1 - i][N - 1 - j]
            A[N - 1 - i][N - 1 - j] = A[j][N - 1 - i]
            A[j][N - 1 - i] = temp
    return  A

def mainDiagonal(mat):
    for i in range(len(mat)):
        for j in range(i + 1):
            temp = mat[i][j]
            mat[i][j] = mat[j][i]
            mat[j][i] = temp
    return mat


def reverseDiagonal(mat):
    for i in range(len(mat)):
        for j in range(len(mat) - i):
            tmp = mat[i][j]
            mat[i][j] = mat[(len(mat) - 1) - j][(len(mat) - 1) - i]
            mat[(len(mat) - 1) - j][(len(mat) - 1) - i] = tmp
    return mat

def rotateMatrix(mat, N):
    for x in range(0, int(N / 2)):

        for y in range(x, N - x - 1):
            temp = mat[y][x]

            mat[y][x] = mat[N - 1 - x][y]

            mat[N - 1 - x][y] = mat[N - 1 - y][N - 1 - x]

            mat[N - 1 - y][N - 1 - x] = mat[x][N - 1 - y]

            mat[x][N - 1 - y] = temp
    return mat


def flipimage(mat):
    for i in range(len(mat)):
        for j in range(i + 1):
            temp = mat[i][j]
            mat[i][j] = mat[j][i]
            mat[j][i] = temp
    return mat


def flipimage2(mat):
    for i in range(len(mat)):
        for j in range(len(mat) - i):
            tmp = mat[i][j];
            mat[i][j] = mat[(len(mat) - 1) - j][(len(mat) - 1) - i];
            mat[(len(mat) - 1) - j][(len(mat) - 1) - i] = tmp
    return mat


def query_matrix(mat, q):
    for i in range(len(q)):
        if q[i] == 0:
            mat = rotateMatrix(mat, len(mat))
        elif q[i] == 1:
            mat = flipimage(mat)
        else:
            mat = flipimage2(mat)
    return mat



#mat = [[1,2,3],[4,5,6],[7,8,9]]
#mat = [[11,2,9,1],[17,4,0,32],[1,7,10,6],[80,3,5,14]]
mat = [[5,5],[1,2]]

'''
mat = rotate90Clockwise(mat).copy()
print(mat)
#print(x)
mat = mainDiagonal(mat).copy()
print(mat)
#print(y)


print(reverseDiagonal(mat))


'''

#print(mainDiagonal(mat))
q = [2,0,2,0,1]
#q = [0,1,2,0]
for i in range(len(q)):
    if q[i] == 0:
        mat = rotate90Clockwise(mat)
    elif q[i] == 1:
        mat = mainDiagonal(mat)
    else:
        mat = reverseDiagonal(mat)
    print(q[i],mat)
print("-----------------------------")