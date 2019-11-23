def print_factors(x):
    factors = []
    #print("The factors of",x,"are:")
    for i in range(1, x):
        if x % i == 0:
            factors.append(i)
            #print(i)
    return factors

temp = [3,6,7,21,100]
q = []
for i in range(len(temp)):
    f  = print_factors(temp[i])
    if len(f)==3:
        res = 1
        for i in range(len(f)):
            res = res * f[i]
        q.append(res)


print("Final Output",sum(q))



