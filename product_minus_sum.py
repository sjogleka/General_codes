def getProduct(n):
    product = 1
    while (n != 0):
        product = product * (n % 10)
        n = n // 10
    print(product)
    return product

def sumList(n):
    sum = 0
    while (n != 0):
        sum = sum + (n % 10)
        n = n // 10
    print(sum)
    return sum

# = 123456
n = 1010
print(getProduct(n)-sumList(n))