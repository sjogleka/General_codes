n = 3
boxes = [1,2,3]
#boxes =[7,4,7]#39
#boxes = [3,2,1]#15
#boxes = [4,7,2]
total_time = 0

'''
for i in range(0,len(boxes)):
    if boxes[i]>0:
        travel_time = (n-i) * boxes[i]
        count = boxes[i]
        print("Travel Time: ",travel_time)
        for j in range(i+1,len(boxes)):
            if boxes[j] != 0:
                if boxes[j]<boxes[i]:
                    count+=boxes[j]
                    boxes[j] = 0
                elif boxes[j]>=boxes[i]:
                    count+=boxes[i]
                    boxes[j] = boxes[j]-boxes[i]
        total_time += travel_time+count
        print(total_time)
        boxes[i] = 0
        count = 0
'''

def test(boxes):
    sumOfboxes = sum(boxes)
    maxNum = boxes[0]
    if boxes[0]!=0:
        travel_time= boxes[0]*(len(boxes))
    else:
        travel_time = 0
    for i in range(1,len(boxes)):
        if boxes[i]!=0:
            if boxes[i]>maxNum:
                travel_time+=(boxes[i]-maxNum)*(n-i)
        if boxes[i]>maxNum:
            maxNum = boxes[i]

    print("Travel Time",travel_time,"sum of boxes",sumOfboxes)
    return sumOfboxes+travel_time


#print(total_time)

print(test(boxes))



