def pascalTriangel(n):
    if n ==0:
        return 1
    if n ==1:
        return [1,1]
    res  = [[1],[1,1]]
    for i in range(2,n):
        temp = res[i-1]
        arr = [0]*(i+1)
        arr[0] = 1
        arr[i] = 1
        for j in range(1,i):
            #print(temp[j-1],temp[j])
            arr[j] = temp[j-1]+temp[j]
        res.append(arr)
    return res
if __name__ == '__main__':
    height = int(input("height ?"))
    createdPascal = pascalTriangel(height)
    print("Created Pascal Triangle",createdPascal)
    row = int(input("row ?"))
    column = int(input("column ?"))
    print(createdPascal[height-row][column])
    print(createdPascal[height-row])
