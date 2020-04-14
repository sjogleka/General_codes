def longestIncreasingPath(matrix):
    tempq = 0
    def dfs(i,j,path,ret1):
        x= [1,-1,0,0]
        y = [0,0,1,-1]
        num = matrix[i][j]
        matrix[i][j] = -1

        for m in range(4):
            new_i = i + x[m]
            new_j = j + y[m]
            if 0<=new_i<r and 0<=new_j<c and matrix[new_i][new_j]>num:
                ret1.append(dfs(new_i,new_j,path+[matrix[new_i][new_j]],ret1))
                #print("After",ret1)


        matrix[i][j] = num
        print(path)

        return len(path)


    r = len(matrix)
    c =len(matrix[0])
    pathLength = 0
    ret = []
    for i in range(r):
        for j in range(c):
            print("......",nums[i][j],'......')
            path = [nums[i][j]]
            dfs(i,j,path,ret)
    print(max(ret))


if __name__ == '__main__':
    #nums = [[9,9,4],[6,6,8],[2,1,1]]
    nums = [[3,4,5],[3,2,6],[2,2,1]]
    longestIncreasingPath(nums)
