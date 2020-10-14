import copy
def matrix_summation(matrix):
    if not len(matrix):
        return

    op = copy.deepcopy(matrix)
    for i in range(len(op)):
        for j in range(len(op[0])):
            op[i][j] = 0
            
    op[0][0] = matrix[0][0]
    #print(op)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i ==0 and j ==0:
                continue
            s = matrix[i][j]
            for x in range(i+1):
                for y in range(j+1):
                    #print(x,y)
                    s = s-op[x][y]
            op[i][j] = s

    #print(op)
    return op


matrix_summation([[2,5],[7,17]])
matrix_summation([[1,2],[3,4]])
matrix_summation([[2,1],[5,4]])
matrix_summation([[33,94,56,34,77],[89,27,55,74,3],[38,20,90,45,60],[98,65,58,18,14],[2,64,11,1,79],[4,67,78,13,53],[98,68,90,2,62],[13,1,34,75,95],[23,16,39,95,42]])
#matrix_summation([])
#matrix_summation([[1,2,3],[4,5,6],[7,8,9]])
#matrix_summation([[1,2],[4,5],[7,8]])
#matrix_summation([[1,2,4],[1,3,4]])