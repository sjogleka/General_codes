import collections
'''
def FindCriticalNodes(numEdges, numNodes, edges):
    # Get all the node
    nodes = []
    for i in range(numEdges):
        # Get nodes
        if edges[i][0] not in nodes:
            nodes.append(edges[i][0])

        if edges[i][1] not in nodes:
            nodes.append(edges[i][1])

    # Get all the neighbours
    neighbours = {node: [] for node in nodes}
    for i in range(numEdges):
        # Get neighbours
        neighbours[edges[i][0]].append(edges[i][1])
        neighbours[edges[i][1]].append(edges[i][0])

    def dfs(parent, seen):
        nonlocal neighbours
        # print("Visiting node {}".format(parent))

        # Mark the parent as explored
        seen[parent] = 1

        # Get all the neighbours from parent
        neig = neighbours[parent]

        # Iterate all the neighbours
        for i in range(len(neig)):
            # return if this node was exlored
            if seen[neig[i]] == 1:
                continue

            # DFS
            dfs(neig[i], seen)

    # Loop over all the nodes
    output = []
    for i in range(numNodes):
        explored = {node: 0 for node in nodes}

        # Mark the cutting point as explored as we
        # don't wanna explore this point
        explored[nodes[i]] = 1

        # DFS
        # Traverse from 0 every time
        total_visited = 1
        dfs(nodes[0], explored)

        print("Node {}: Explores {} nodes.".format(nodes[i], sum(explored.values())))
        # If all nodes are explored, it means it's not articulate point
        if (sum(explored.values()) < numNodes):
            output.append(nodes[i])

    print(neighbours, nodes)
    print(output)


if __name__ == "__main__":
    numNodes, numEdges = 7, 7
    #edges = [[0, 1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3, 4]]
    edges = [[1, 2], [1, 3], [2, 4], [3, 4], [3, 6], [6, 7], [4, 5]]
    FindCriticalNodes(numNodes, numEdges, edges)

'''

# Input:
# numNodes = 7,
# numEdges = 7,
# edges = [[0, 1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3, 4]]
# Output:
# [2, 3, 5]

def findcriticalnodes(n, edges):
    g = collections.defaultdict(list)
    for conn in edges:
        g[conn[0]].append(conn[1])
        g[conn[1]].append(conn[0])
    visited = [0] * n
    isarticulationpoints = [0] * n
    order = [0] * n
    low = [0] * n
    seq = 0

    def dfs(u, p):
        nonlocal seq
        visited[u] = 1
        order[u] = low[u] = seq
        seq = seq + 1
        children = 0
        for to in g[u]:
            if to == p:
                continue
            if visited[to]:
                low[u] = min(low[u], low[to])
            else:
                dfs(to, u)
                low[u] = min(low[u], low[to])
                if order[u] <= low[to] and p != -1:
                    isarticulationpoints[u] = 1
                children += 1

        if p == -1 and children > 1:
            isarticulationpoints[u] = 1

    dfs(0, -1)
    ans = []
    for i in range(len(isarticulationpoints)):
        if isarticulationpoints[i]:
            ans.append(i)
    return ans


if __name__ == "__main__":
    a = [[1, 2], [1, 3], [2, 4], [3, 4], [3, 6], [6, 7], [4, 5]]
    print(findcriticalnodes(7, a))