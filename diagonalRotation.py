def diagonalRotation(matrix):
    s = set()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i!=j and (i+j)!=len(matrix)-1 and (j,i) not in s:
                matrix[i][j],matrix[j][i] = matrix[j][i], matrix[i][j]
                s.add((i,j))

    for i in range(len(matrix)):
        temp = matrix[i]
        s2 = set()
        for j in range(len(temp)):
            if i!=j and (i+j) != len(matrix)-1 and j not in s2 and (len(temp)-1-j) not in s2:
                print(i,j)
                temp[len(temp)-1-j], temp[j] = temp[j], temp[len(temp)-1-j]
                s2.add(j)
                s2.add(len(temp)-1-j)
        matrix[i] = temp
    return matrix

'''
def rotateMatrix(matrix):
    length = len(matrix[0])
    for i in range(length // 2):
        for j in range(i, length - i - 1):
            if i != j:
                temp = matrix[i][j]
                matrix[i][j] = matrix[length - 1 - j][i]
                matrix[length - 1 - j][i] = matrix[length - 1 - i][length - 1 - j]
                matrix[length - 1 - i][length - 1 - j] = matrix[j][length - 1 - i]
                matrix[j][length - 1 - i] = temp
                # end if
    return matrix


def rotateOverDiagonals(m, k):
    for i in range(k):
        m = rotateMatrix(m)

    print(m)
'''


if __name__ == '__main__':
    m = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
    #m = [[1,2,3],[4,5,6],[7,8,9]]
    k  =1
    for i in range(k):
        m = diagonalRotation(m)
    print(m)
    #print(rotateOverDiagonals(m,1))