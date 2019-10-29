from math import sqrt

def chkprime(numberToCheck):
    if numberToCheck == 1:
        return False
    for i in range(2, int(sqrt(numberToCheck)) + 1):
        if numberToCheck % i == 0:
            return False

    return True

def primeSum(l, r):
    sum = 0

    for i in range(r, (l - 1), -1):
        isPrime = chkprime(i)
        if (isPrime):
            sum += i
    return sum

if __name__ == "__main__":
    l = input()
    r = input()

    print (l)

    #l, r = 4, 13

    # Call the function with l and r
    print(primeSum(int(l), int(r)))

#primeSum(X,Y)
### Function la call kar
