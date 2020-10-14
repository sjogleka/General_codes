def variantsCount(n,s0,k,b,m,a):
    s = [0 for _ in range(1000000001)]
    s[0] = s0
    for i in range(1,n):
        s[i]=(k*s[i-1]+b)
        s[i] = s[i]%m
        s[i] = s[i]+1+s[i-1]

    count = 0
    l = 0
    r = n-1
    while l<r:
        if s[l]*s[r]<=a:
            count+=1
        l+=1
        r-=1
    return count

print(variantsCount(3,1,1,1,2,4))