def matrix(x):
    n = len(x)
    temp = []
    for i in range(n):
        for j in range(n):
            if i==0 or j==0 or i==n-1 or j==n-1:
                temp.append(x[i][j])



if __name__ == '__main__':
    x = [[9,7,4,5],[1,6,2,-6],[12,20,2,0],[-5,-6,7,-2]]
    print(len(x))
    matrix(x)


