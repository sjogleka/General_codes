def getMinTrips(weights,max_size):
    weights.sort()
    i = len(weights)
    trips = 0
    curr_weight = 0
    while i > 0:
        if curr_weight + weights[i-1] <= max_size:
            curr_weight += weights[i-1]
            i-=1
        else:
            trips += 1
            curr_weight = 0
    return trips

def getMinTrips_1(a):
    j, trips = 0, 0
    while j < len(a) - 1:
        if a[j] + a[j + 1] <= 3.00:
            trips += 1
            j += 2
            if (j == len(a) - 1):
                trips += 1
                break
            else:
                continue
        else:
            trips += 1
            j += 1
    print(trips)


print(getMinTrips([1.01,1.99,2.5,1.5,1.01],3))
print(getMinTrips([1.01,1.01,1.01,1.4,2.4],3))
print(getMinTrips([1.01,1.991,1.32,1.4],3))



print(getMinTrips_1([1.01,1.99,2.5,1.5,1.01]))
print(getMinTrips_1([1.01,1.01,1.01,1.4,2.4]))
print(getMinTrips_1([1.01,1.991,1.32,1.4]))