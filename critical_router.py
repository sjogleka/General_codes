from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices + 1
        self.adj_list = defaultdict(list)
        self.parent = [-1] * self.V
        self.low = [float('inf')] * self.V
        self.disc = [float('inf')] * self.V
        self.visited = [False] * self.V
        self.time = 0
        self.bridges = []

    def add_edge(self, v, u):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def find_bridges(self, u):
        self.visited[u] = True
        self.low[u] = self.time
        self.disc[u] = self.time
        self.time += 1
        for v in self.adj_list[u]:
            if not self.visited[v]:
                self.low[u] = min(self.low[u], self.low[v])
                if self.low[v] > self.disc[u]:
                    self.bridges.append([u, v])

            elif v != self.parent[u]:
                self.low[u] = min(self.low[u], self.disc[v])


def criticalConnection(numOfWarehouses, numOfRoads, roads):
    ans = []
    adj_list = defaultdict(list)
    for s, d in roads:
        adj_list[s].append(d)
        adj_list[d].append(s)
    for s, d in roads:
        adj_list[s].remove(d)
        adj_list[d].remove(s)
        if len(dfs(s, adj_list, set())) != numOfWarehouses:
            ans.append((s, d))
        adj_list[s].append(d)
        adj_list[d].append(s)
    return ans

def dfs(s, adj_list, visited):
    visited.add(s)
    for d in adj_list[s]:
        if d not in visited:
            dfs(d, adj_list, visited)
    return visited

if __name__ == '__main__':
    g = Graph(7)
    edges = [[1, 2], [1, 3], [2, 4], [3, 4], [3, 6], [6, 7], [4, 5]]
    #edges = [[1, 2], [1, 3], [2, 3], [3, 4], [3, 6], [4, 5], [6, 7], [6, 9], [7, 8], [8, 9]]
    #edges = [[1, 2], [1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [5, 6], [5, 7], [6, 7], [7, 8],[8,9],[8,10],[9,10]]
    #edges = [[1, 2], [2, 3], [3, 4], [4, 5], [6, 3]]
    #edges = [[1, 2], [1, 3], [3, 4], [1, 4], [4, 5]]
    #edges = [[1, 2], [2, 3], [3, 4], [4, 5], [6, 3]]

    for i in edges:
        g.add_edge(i[0], i[1])

    for j in range(1, g.V):
        if not g.visited[j]:
            g.find_bridges(j)

    print(g.adj_list)
    print(sorted(g.bridges))


    print(criticalConnection(5,6,edges))