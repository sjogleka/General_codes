def topological_sort(vertex,op,visited,d):
    print(vertex,'-----------',visited)
    if not visited[vertex]:
        visited[vertex] = True
        for i in d[vertex]:
            topological_sort(i,op,visited,d)
        op.append(vertex)
        print(vertex,visited)




if __name__ == '__main__':
    d = {
        0: [],
        1: [],
        2: [3],
        3: [1],
        4: [0, 1,5],
        5: [2, 0]
    }
    output_stack = []
    recStack = [False]*len(d)
    visited = [False]*len(d)

    for k,v in d.items():
        topological_sort(k,output_stack, visited, d)


    print(output_stack)










