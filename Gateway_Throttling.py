
def droppedRequest(RequestTime):
    D = {}
    drop_count = 0
    for i in RequestTime:
        if i in D:
            D[i] += 1
        else:
            D[i] = 1
        drop_count = 0
        time = [i for i in D]
        time = sorted(time)
        for i in time:
            drop_count += max(D[i]-3,0)
            drop_count += max(sum([D[i] for i in range(max(min(time),i-9),i+1) if i in D])-20,0)
            drop_count += max(sum([D[i] for i in range(max(min(time),i-59),i+1) if i in D])-60,0)
    return drop_count

def droppedRequests(requestTime):
    freq = dict()
    for r in requestTime:
        if r in freq.keys():
            freq[r] = freq[r] + 1
        else:
            freq[r] = 1
    of = sorted(freq.items(), key=lambda x: x[0])
    print(of)
    dropped = 0
    of2 = dict()
    for k, v in of:
        if v > 3:
            dropped = dropped + v - 3
            of2[k] = 3
        else:
            of2[k] = v
    #print("-single second -")
    x1 = dropped
    #print(dropped)
    #rint(of2)

    dropped = 0  ######################

    # run 10 seconds and make of3
    of3 = dict()
    for k in of2.keys():
        start = k
        ten_end = k + 9
        ten_second = 0
        for k2 in of2.keys():
            if start <= k2 <= ten_end:
                ten_second = ten_second + of2[k2]
                if ten_second > 20:
                    x = of2[k2] - (ten_second - 20)
                    if x > 0:
                        of3[k2] = x
                    else:
                        of3[k2] = 0
                else:
                    of3[k2] = of2[k2]
            if k2 > ten_second:
                break
        if ten_second > 20:
            dropped = dropped + ten_second - 20
    y1 = dropped
    #print(of3)

    dropped = 0  ######################

    for k in of3.keys():
        start = k
        minute_end = k + 59
        one_minute = 0
        for k3 in of3.keys():
            if start <= k3 <= minute_end:
                one_minute = one_minute + of3[k3]
            if k3 > minute_end:
                break
        if one_minute > 60:
            dropped = dropped + one_minute - 60
    z1 = dropped
    #print(x1)
    #print(y1)
    #print(z1)
    #print(x1 + y1)
    ans = 0


    if x1 > 0:
        ans += x1
    if y1 > 0:
        ans += x1 + y1
    if z1 > 0:
        ans += z1 + y1+ x1

    print(ans)

    return ans

class Graph:

    # init function to declare class variables
    def __init__(self, V):
        self.V = V
        self.adj = [[] for i in range(V)]

    def DFSUtil(self, temp, v, visited):
        # Mark the current vertex as visited
        visited[v] = True

        #print(v)

        # Store the vertex to list
        temp.append(v)

        # Repeat for all vertices adjacent
        # to this vertex v
        for i in self.adj[v]:
            if visited[i] == False:
                # Update the list
                temp = self.DFSUtil(temp, i, visited)

        return temp

    # method to add an undirected edge
    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)

    # Method to retrieve connected components
    # in an undirected graph
    def connectedComponents(self):
        visited = []
        cc = []
        for i in range(self.V):
            visited.append(False)
        for v in range(self.V):
            if visited[v] == False:
                temp = []
                cc.append(self.DFSUtil(temp, v, visited))
        return cc

    # Driver Code

#def totalNoEdges(arr, comp_from, comp_to):

def totalEdges(cc , comp_from, comp_to):
    if len(cc) < 2:
        return 0
    j = 0
    edges = 0
    while j < len(comp_from):
        if comp_from[j] in cc and comp_to[j] in cc:
            edges += 1
        j += 1

    return edges

#print(totalEdges([0,1,2],[0,0,2],[1,2,1]))


    # Create a graph given in the above diagram
    # 5 vertices numbered from 0 to 4
def minOperations(comp_nodes, comp_from, comp_to):
    g = Graph(comp_nodes);
    i =0
    comp_from = [x - 1 for x in comp_from]
    comp_to = [x - 1 for x in comp_to]
    while i < len(comp_from):
        g.addEdge(comp_from[i], comp_to[i])
        i +=1

    #g.addEdge(0, 1)
    #g.addEdge(0, 2)
    #g.addEdge(2, 1)
    cc = g.connectedComponents()
    #print("Following are connected components")
    #print(cc)
    r = []
    i = 1
    for eachCC in cc:
        r.append(totalEdges(eachCC,comp_from,comp_to)- (i-1))
        i += 1
    if sum(r) > len(cc) -1:
        return len(cc) -1
    else:
        return -1

print(minOperations(4, [1, 1, 3], [2, 3, 2]))
#RequestTime = [1,1,1,1,2,2,2,3,3,3,4,4,4,11,11,11,6,6,6,5,5,5]
RequestTime = [1,1,1,1,2]
drop_count = droppedRequest(RequestTime)
#print(drop_count)


droppedRequests(RequestTime)

