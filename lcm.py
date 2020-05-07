def gcd(a,b):
    #print("......",a,b,"......")
    if a == 0:
        return b

    return gcd(b%a,a)

def lcm(a,b):
    if a ==0 or b ==0:
        return 0
    print(gcd(a,b))
    return (a*b)//gcd(a,b)


if __name__ == '__main__':
    #print(gcd(20,30))
    #print(gcd(30,20))

    print(lcm(2,51))


