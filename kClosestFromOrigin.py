import  math, operator
def distance(x,y):
    return int(math.sqrt(x**2+y**2))

def kClosest(points,k):
    d = {}
    op = []
    for i in range(len(points)):
        x = points[i][0]
        y = points[i][1]

        d[i] = distance(x,y)

    res = sorted(d.items(),key=lambda x:(x[1],x[0]))[:k]
    for i in range(k):
        op.append(points[res[i][0]])

    return op








if __name__ == '__main__':
    #points = [[3, 3], [5, -1], [-2, 4]]
    points = [[1, 3], [-2, 2]]
    #K = 2
    K = 1
    print(kClosest(points,K))