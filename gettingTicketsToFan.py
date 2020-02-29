


if __name__ == '__main__':
    worldSize = input()
    numberOfEvents = input()
    events = {}
    tickets ={}
    def manhattan_distance(x1,y1,x2,y2):
        return abs(x1-x2)+abs(y1-y2)

    for i in range(1,int(numberOfEvents)+1):
        eventDesc = list(map(int,input().split()))
        events[i] = [eventDesc[1],eventDesc[2]]
        tickets[i] = eventDesc[3:]

    noOfBuyers = input()
    buyers =[]
    for i in range(1,int(noOfBuyers)+1):
        buyer = list(map(int,input().split()))
        buyers.append(buyer)

    print("Events:- ",events)
    print("Tickets: - ",tickets)
    print("Buyers: -",buyers)
    dist = {}
    for i in range(len(buyers)):
        mindis = 100000
        for j in range(len(events)):
            print(events[j+1])
            tempdis = manhattan_distance(events[j+1][0],events[j+1][1],buyers[i][0],buyers[i][1])
            if tempdis < mindis:
                mindis = tempdis
                eventNo  = j+1
            elif tempdis == mindis:
                minTicket = min(min(tickets[eventNo]),min(tickets[j+1]))
                if minTicket == min(tickets[j+1]):
                    dist[i] = minTicket
                else:
                    dist[i] = minTicket
                tickets[j + 1].remove[minTicket]

    print(dist)



