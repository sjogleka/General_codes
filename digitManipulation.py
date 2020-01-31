def digitManipulations(n):
    n = str(n)
    product = 1
    sum1 =0
    for i in range(len(n)):
        product = product *int(n[i])
        sum1 = sum1 +int(n[i])


    print(product-sum1)


if __name__ == '__main__':
    digitManipulations(123456)
    digitManipulations(1010)
