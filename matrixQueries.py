import math
def createMatrix(n,m):
    Matrix = [[x*y for x in range(1,n+1)] for y in range(1,m+1)]
    return Matrix

def matrixquery(n,m,queries):
    result=[]
    min_row=1
    row=[]
    min_column=1
    col=[]
    for query in queries:
        if query[0] == 0:
            result.append((min_row)*(min_column))
        elif query[0] == 1:
            row.append(query[1])
            for i in range(1,n+1):
                if i not in row:
                    min_row=i
                    break
        else:
            col.append(query[1])
            for i in range(1,m+1):
                if i not in col:
                    min_column=i
                    break
        print(min_row,min_column)
    return result


def matrixquery(n,m,queries):
    matrix=[]
    result=[]
    for i in range(0,n):
        matrix.append([])
        for j in range(0,m):
            matrix[i].append((i+1)*(j+1))
    for query in queries:
        if query[0] == 0:
            mini = min(min(matrix))
            result.append(mini)
        elif query[0] == 1:
            for i in range(0,m):
                matrix[query[1]-1][i] = math.inf
        else:
            for i in range(0,n):
                matrix[i][query[1]-1] = math.inf
    print(matrix)
    return result



matrix = createMatrix(3,3)
print(matrix)
print(min(min(matrix)))
res = []
#n = 10
#m = 2
#n = 100000
#m = 100000
n = 3
m = 4
queries  = [[0],[1,2],[0],[2,1],[0],[1,1],[0]]
#queries  = [[1,1],[2,2],[0]]
#queries = [[0]]
#print(matrixquery(n,m,queries))



def matrixLogic(n, m, queries):
    row = []
    col = []
    mini = []

    for i in range(1,n+1):
        row.append(i)

    for j in range(1,m+1):
        col.append(j)

    print(row, col)

    for query in queries:
        if query[0] == 0:
            mini.append(row[0]*col[0])
        elif query[0] == 1:
            row.remove(query[1])
        elif query[0] == 2:
            col.remove(query[1])

    return mini

print(matrixLogic(n,m,queries))

