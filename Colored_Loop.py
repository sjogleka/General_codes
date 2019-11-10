def color_loop(n,m,mat):
    for i in range(n-1):
        for j in range(m):
            #print(i,j)
            c = mat[i][j]
            for k in range(j+1,m):
                if mat[i][k] != c:
                    break
            k-=1
            if k>j:
                for l in range(i+1,n-1):
                    #print(l,k)
                    if mat[l][k] != c:
                        break
                l-=1
                print(l,i)
                if l>i:
                    p=k
                    while p-j >= 0:
                        if mat[l][p] != c:
                            break
                        p -= 1
                    p+=1
                    if p == j:
                        q=l
                        while q >= i:
                            if mat[q][p] != c:
                                break
                            q-=1
                        q+=1
                        if q==i:
                            return True
    return False
x = [
    ['B','B','B','B','B','B','B'],
    ['B','R','G','G','G','B','B'],
    ['B','G','B','B','G','B','B'],
    ['B','G','G','G','G','B','B'],
    ['B','B','B','B','B','B','B'],
    ['B','B','B','B','B','B','B']
]
print(color_loop(7,6,x))