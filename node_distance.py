
## Incomplete code


def nodeDistance(g_nodes,g_edges, g_from, g_to):
    graph = [[] for _ in range((g_nodes+1))]
    cycles = [[] for _ in range((g_nodes+1))]
    nodes = set()
    color = [0] * (g_edges+1)
    par = [0] * (g_edges+1)
    mark = [0] * (g_edges+1)
    cyclenumber = 0
    edges = g_edges

    def dfs_cycle(graph, u, p, color,mark, par):
        global cyclenumber

        # already (completely) visited vertex.
        if color[u] == 2:
            return

        # seen vertex, but was not
        # completely visited -> cycle detected.
        # backtrack based on parents to
        # find the complete cycle.
        if color[u] == 1:
            cyclenumber += 1
            cur = p
            mark[cur] = cyclenumber

            # backtrack the vertex which are
            # in the current cycle thats found
            while cur != u:
                cur = par[cur]
                mark[cur] = cyclenumber

            return

        par[u] = p

        # partially visited.
        color[u] = 1

        # simple dfs on graph
        for v in graph[u]:

            # if it has not been visited previously
            if v == par[u]:
                continue
            dfs_cycle(graph, v, u, color, mark, par)

            # completely visited.
        color[u] = 2

    def printCycles(edges, mark: list):
        cycle = []
        for i in range(1, edges + 1):
            if mark[i] != 0:
                cycle[mark[i]].append(i)
        return cycle


    for start,end in zip(g_from,g_to):
        graph[start].append(end)
        nodes.add(start)
        nodes.add(end)

    dfs_cycle(graph,1, 0, color, mark, par)
    print("edges",edges,"mark",mark)
    cycle = printCycles(edges, mark)

    print("cycle",cycle)
    #getDistance(graph,cycle,[1,2,3,4,5,6])
    res = []
    for ele in nodes:
        q = [(ele,0)]
        visited = set()
        while q:
            print(q,res)
            node,distance = q.pop(0)
            if node not  in visited:
                visited.add(node)
                if node in cycle:
                    res.append(distance)
                    break
                else:
                    for item in graph[node]:
                        if item not  in visited:
                            q.append((item,distance+1))

    print(res)
'''
N = 5

graph = [[] for i in range(N)]
cycles = [[] for i in range(N)]

def dfs_cycle(u, p, color: list,mark: list, par: list):
    global cyclenumber
    if color[u] == 2:
        return
    if color[u] == 1:
        cyclenumber += 1
        cur = p
        mark[cur] = cyclenumber
        while cur != u:
            cur = par[cur]
            mark[cur] = cyclenumber

        return

    par[u] = p
    color[u] = 1

    for v in graph[u]:
        if v == par[u]:
            continue
        dfs_cycle(v, u, color, mark, par)
    color[u] = 2


# add the edges to the graph
def addEdge(u, v):
    graph[u].append(v)
    graph[v].append(u)


# Function to print the cycles
def printCycles(edges, mark: list):
    cycle = []

    for i in range(1, edges + 1):
        print(edges, mark)
        if mark[i] != 0:
            cycles[mark[i]].append(i)

            # print all the vertex with same cycle
    for x in cycles[1]:
        cycle.append(x)

    return cycle
        # Driver Code


def getDistance(graph,cycle,nodes):
    res = []
    for ele in nodes:
        q = [(ele,0)]
        visited = set()
        while q:
            print(q,res)
            node,distance = q.pop(0)
            if node not  in visited:
                visited.add(node)
                if node in cycle:
                    res.append(distance)
                    break
                else:
                    for item in graph[node]:
                        if item not  in visited:
                            q.append((item,distance+1))

    print(res)
'''

if __name__ == "__main__":
    # add edges
    '''
    addEdge(1, 2)
    addEdge(2, 3)
    addEdge(1, 3)
    addEdge(3, 5)
    addEdge(1, 4)
    addEdge(2, 6)
    
    addEdge(1, 3)
    addEdge(4, 3)
    addEdge(4, 2)
    addEdge(1, 2)

    #

    color = [0] * N
    par = [0] * N

    # mark with unique numbers
    mark = [0] * N

    # store the numbers of cycle
    cyclenumber = 0
    edges = 4

    # call DFS to mark the cycles
    dfs_cycle(1, 0, color, mark, par)

    # function to print the cycles
    getDistance(graph,printCycles(edges, mark),[1,2,3,4])
    '''
    nodeDistance(6,6,[1,2,1,3,1,2],[2,3,3,5,4,6])

