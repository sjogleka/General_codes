from collections import defaultdict

class Solution:
    def criticalConnections(self, n, connections):
        currentRank = 0  ## please note this rank is NOT the num (name) of the vertex itself, it is the order of your DFS level

        lowestRank = [i for i in
                      range(n)]  ## here lowestRank[i] represents the lowest order of vertex that can reach this vertex i

        visited = [False for _ in range(n)]  ## common DFS/BFS method to mark whether this node is seen before
        graph = defaultdict(list)
        for v in connections:
            graph[v[0]].append(v[1])
            graph[v[1]].append(v[0])
        print(graph)

        res = []
        prevVertex = -1  ## This -1 a dummy. Does not really matter in the beginning.
        ## It will be used in the following DFS because we need to know where the current DFS level comes from.
        ## You do not need to setup this parameter, I setup here ONLY because it is more clear to see what are passed on in the DFS method.

        currentVertex = 0  ## we start the DFS from vertex num 0 (its rank is also 0 of course)
        self._dfs(res, graph, lowestRank, visited, currentRank, prevVertex, currentVertex)
        return res


    def _dfs(self, res, graph, lowestRank, visited, currentRank, prevVertex, currentVertex):
        visited[currentVertex] = True  # it is possible
        lowestRank[currentVertex] = currentRank

        for nextVertex in graph[currentVertex]:
            if nextVertex == prevVertex:
                continue  ## do not include the the incoming path to this vertex since this is the possible ONLY bridge (critical connection) that every vertex needs.

            if not visited[nextVertex]:
                self._dfs(res, graph, lowestRank, visited, currentRank + 1, currentVertex, nextVertex)
            # We avoid visiting visited nodes here instead of doing it at the beginning of DFS -
            # the reason is, even that nextVertex may be visited before, we still need to update my lowestRank using the visited vertex's information.

            lowestRank[currentVertex] = min(lowestRank[currentVertex], lowestRank[nextVertex])
            # take the min of the current vertex's and next vertex's ranking
            if lowestRank[
                nextVertex] >= currentRank + 1:  ####### if all the neighbors lowest rank is higher than mine + 1, then it means I am one connecting critical connection ###
                res.append([currentVertex, nextVertex])

class Solution1:
    def criticalConnections(self, n, connections):
        graph = defaultdict(list)
        for v in connections:
            graph[v[0]].append(v[1])
            graph[v[1]].append(v[0])
        print(graph)
        pre = [-1 for i in range(1,n+1)]
        low = [-1 for i in range(1,n+1)]
        order = 1
        ans = []
        def dfs(par, cur, order):  # pass in parent node, current node and order
            order += 1
            pre[cur+1] = order
            low[cur+1] = pre[cur+1]
            for w in graph[cur]:
                if (pre[w+1] == -1):
                    dfs(cur, w, order)
                    low[cur+1] = min(low[cur+1], low[w+1])
                    if (low[w+1] == pre[w+1]):
                        ans.append((cur, w))

                elif (w != par):
                    low[cur+1] = min(low[cur+1], pre[w+1])

                dfs(1, 1, 0)  # only need to start from one node, since from one node you can reach any other nodes in an undirected graph, dfs(1, 1, 0) will also work
        print(ans)
        return ans

if __name__ == '__main__':
    n = 7
    #edges = [[1, 2], [1, 3], [3, 4], [1, 4], [4, 5]]
    #edges = [[1, 2], [1, 3], [3, 4], [1, 4], [4, 5]]
    #edges = [[1,2],[1,3],[2,3],[3,4],[4,5],[4,6],[5,6],[5,7],[6,7],[7,8],[8,9],[9,10]]
    #edges = [[1,2],[2,3],[3,4],[4,5],[6,3]]
    edges = [[1, 2], [1, 3], [2, 4], [3, 4], [3, 6], [6, 7], [4, 5]]
    solution = Solution()
    print(solution.criticalConnections(n, edges))
