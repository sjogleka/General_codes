'''
Sample Input 1
5
2
1 1 1 40 60
2 1 4 50
3
3 3
3 2
4 3

Sample Input 2
5
2
1 1 1 40
2 1 4 50
1
3 3

Sample Input 3
6
3
1 1 2 100 100 400
2 2 4 100 200 500
3 3 1 100 200 500
3
3 3
3 3
3 3

Sample Input 4
3
2
1 2 2 100 200 400
2 1 4 40 100 200
1
2 2

Sample Input 5
4
2
1 1 2 100 200 400
2 2 4 100 200 400
2
3 3
3 3

Sample Input 6
2
1
1 2 2 60 15 90
1
2 2

Sample Input 7
2
1
1 2 2 60 15 90
1
2 2

Sample Input 8
3
2
2 2 2 400 100 200
1 4 4 40 100 200
1
2 2


Sample Input 9
7
3
2 4 4 100
1 2 2 100
3 1 3 100
4
3 3
3 3
3 3
3 3

'''
import math
def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

sizeOfWorld = int(input())
numberOfEvents = int(input())
events = {}
buyer = []
ticket = {}
op = []
dist = {}
eventId = 0

for i in range(0, numberOfEvents):
    eventLine = input()
    eventLine = list(map(int, eventLine.split()))
    events[eventLine[0]] = [eventLine[1], eventLine[2]]
    ticket[eventLine[0]] = sorted(eventLine[3:])

numberOfBuyers = int(input())
for i in range(0, numberOfBuyers):
    buyerLine = input()
    buyerLine = list(map(int, buyerLine.split()))
    buyer.append(buyerLine)
print("Events:-",events,"Tickets: -",ticket,"Buyer: -",buyer)
#print("-----------------------------------------------------")
for i in range(int(numberOfBuyers)):
    minDist = math.inf
    coOrdinate = buyer[i]
    for k, v in events.items():
        preevent = eventId
        betwDist = manhattan_distance(coOrdinate[0], coOrdinate[1], v[0], v[1])
        #print("Dist",betwDist,v,coOrdinate,minDist)
        if betwDist < minDist and len(ticket[k]) != 0:
            minDist = betwDist
            eventId = k
        elif betwDist == minDist and len(ticket[k]) != 0:
            #print("--------",k,eventId)
            if ticket[k][0]<ticket[eventId][0]:
                eventId = k
            elif ticket[k][0]==ticket[eventId][0] and k<eventId:
                eventId = k

            #print(k, eventId,"--------")

    #print("-------------------------------")
    #print(ticket,eventId)
    if eventId in ticket and ticket[eventId]:
        tickets = ticket[eventId].pop(0)
    else:
        eventId = -1
        tickets = 0
    print(eventId, tickets)

'''
# The following method get the manhatten distance betwen two points (x1,y1) and (x2,y2)
import math
def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


# Enter your code here. Read input from STDIN. Print output to STDOUT
sizeOfWorld = int(input())
numberOfEvents = int(input())
events = {}
buyer = []
ticket ={}
op = []
dist ={}
eventId = 0

for i in range(0,numberOfEvents) :
    eventLine = input()    
    eventLine = list(map(int,eventLine.split()))
    events[i] = [eventLine[0],eventLine[1]]
    ticket[i] = sorted(eventLine[3:])

    
numberOfBuyers = int(input())
for i in range(0,numberOfBuyers) :
    buyerLine = input()
    buyerLine = list(map(int,buyerLine.split()))
    buyer.append(buyerLine)


#print("Events:-",events,"Tickets: -",ticket,"Buyer: -",buyer) 

for i in range(int(numberOfBuyers)):
    minDist  = math.inf
    coOrdinate = buyer[i]
    for k,v in events.items():
        preevent = eventId
        betwDist = manhattan_distance(coOrdinate[0],coOrdinate[1],v[0],v[1])
        if betwDist<=minDist and len(ticket[k])!=0:
            minDist = betwDist
            eventId = k
            minprice = ticket[eventId][0]
        elif betwDist == minDist and len(ticket[k])!=0:
            if minprice > ticket[k][0]:
                eventId = preevent
                minprice = ticket[k][0]
    #print(ticket,eventId)    
    if eventId in ticket and ticket[eventId]:
            tickets = ticket[eventId].pop(0)
        #print(tickets)
    else:
        eventId = -2
        tickets = 0
    print(eventId+1,tickets)
    
# The solution to the first sample above would be to output the following to console:
# (Obviously, your solution will need to figure out the output and not just hard code it)
'''




