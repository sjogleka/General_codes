def nonDegenrateTriangle(a,b,c):
    res = []

    for i in range(len(a)):
        if a[i]<b[i]+c[i] and b[i]<a[i]+c[i] and c[i]<a[i]+b[i]:
            res.append("YES")
        else:
            res.append("NO")
    return res

if __name__ == '__main__':
    a = [7,10,7]
    b = [2,3,4]
    c = [2,7,4]
    #a,b,c = [],[],[]
    print(nonDegenrateTriangle(a,b,c))