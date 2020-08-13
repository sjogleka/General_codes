def almosttettris(n,m,figures):
    matrix = [[0 for _ in range(m)] for _ in range(n)]
    #print(matrix)
    dict = {1:[(0,0)],2:[(0,0),(0,1),(0,2)],3:[(0,0),(0,1),(1,0),(1,1)],4:[(0,0),(1,0),(1,1),(2,0)],5:[(0,1),(1,0),(1,1),(1,2)]}
    for ele in range(len(figures)):
        box = dict[figures[ele]]
        #print(figures[ele])
        flag = False
        for i in range(n):
            for j in range(m):
                if not flag and matrix[i][j] == 0 and checkIfFits(m,n,i,j,box):
                    for k in range(len(box)):
                        print(box[k][0],box[k][1])
                        flag = True
                        matrix[i+box[k][0]][j+box[k][1]] = ele+1
                    break

    print(matrix)

def checkIfFits(m,n,i,j,box):
    if len(box) ==0:
        return True
    if 0<=i+box[0][0]<n and 0<=j+box[0][1]<m:
        return checkIfFits(m,n,i,j,box[1:])
    return False

if __name__ == '__main__':
    almosttettris(4,4,[4,2,1,3])
    almosttettris(2, 3, [5])
