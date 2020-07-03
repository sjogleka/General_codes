import  math
def formTeam(d,t,q):
    tempx = 0
    tempy = 0
    while d>=1:
        d -=1
        tempx += math.factorial(d)

    while t >= 1:
        t -= 1
        tempy += math.factorial(t)

    print(tempx,tempy)

    print((tempx+tempy)//(d+t-q))

if __name__ == '__main__':
    formTeam(3,2,4)