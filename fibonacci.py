def fibo_recursive(n):
    if n ==1:
        return 0
    if n ==2:
        return 1
    else:
        return fibo_recursive(n-1)+fibo_recursive(n-2)

def fibo_iterative(n):
    res = [0, 1]
    if n == 1:
        return [0]
    if n == 2:
        return res
    for i in range(2,n,1):
        res.append(res[i-1] + res[i-2])
    return res


print(fibo_recursive(9))
#print(fibo_recursive(4))
print(fibo_iterative(4))
print(fibo_iterative(3))
print(fibo_iterative(1))
print(fibo_iterative(2))
print(fibo_iterative(9))
print(fibo_iterative(10))


