def segmentCovering(listOfTuples):
    sortedBeg = sorted(listOfTuples, key=lambda x: x[0])
    sortedEnd = sorted(listOfTuples, key=lambda x: x[1])
    print("Sorting on the basis of 1st value: - ",sortedBeg,"\nSorting on the basis of 2nd value: - ",sortedEnd)
    thrhold = sortedBeg[0][0] - 1
    print("Initial threshold: -",thrhold)
    listOfPoints = []
    for i in range(len(sortedEnd) - 1):
        beg, end = sortedEnd[i]
        if beg > thrhold:
            listOfPoints.append(end)
            thrhold = end
            print("Updating Threshold:- ",thrhold)
        if listOfPoints[len(listOfPoints) - 1] < sortedEnd[len(sortedEnd) - 1][0]:
            if sortedEnd:
                print(sortedEnd[len(sortedEnd) - 1][0])
                listOfPoints.append(sortedEnd[len(sortedEnd) - 1][0])
        print((listOfPoints))
    return len(listOfPoints)


def segmentCovering_1(listOfTuples):

    sortedBeg = sorted(listOfTuples, key=lambda x: x[0])
    sortedEnd = sorted(listOfTuples, key=lambda x: x[1])
    print(sortedEnd[len(sortedEnd) - 1])

    thrhold = sortedBeg[0][0] - 1
    listOfPoints = []
    for i in range(len(sortedEnd) - 1):
        beg, end = sortedEnd[i]
        if beg > thrhold:
            listOfPoints.append(end)
            thrhold = end
    print(listOfPoints)

    if(len(listOfPoints)) == 0:return 0

    if listOfPoints[len(listOfPoints) - 1] < sortedEnd[len(sortedEnd) - 1][0]:
        if sortedEnd:
            listOfPoints.append(sortedEnd[len(sortedEnd) - 1][0])
    #print(len(listOfPoints))
    result = []
    for p in listOfPoints:
        result.append(p)

    return len(result)
#segment = [[-1,3],[-5,-3],[3,5],[2,4],[-3,-2],[-1,4],[5,5]]
#segment = [[-2,1], [-1,0], [0,1], [1,2]]
segment = [[-1000000000, 1000000000]]
print(segmentCovering_1(segment))