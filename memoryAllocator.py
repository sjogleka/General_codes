def allocate(arr,index):
    for i in range(len(arr)):
        if len(arr[i:i+index])!=index:
            return -1,arr
        if sum(arr[i:i+index]) ==0:
            arr[i:i+index] = [1]*(i+index-i)
            return i,arr
    return -1,arr

def memoryAllocator(a,queries):
    print("----------------------------------")
    res = []
    counter = 0
    atomic_counter = []
    atomic_index= []
    for i in  range(len(queries)):
        if queries[i][0] == 0:
            #print("---- Adding ----")
            op,a = allocate(a,queries[i][1])
            #print(op)
            if op!=-1:
                counter+=1
                atomic_counter.append(counter)
                atomic_index.append(queries[i][1])
            res.append(op)
            #print(res,atomic_counter)
        else:
            #print("----- Erasing -----")
            #print(atomic_counter)
            if queries[i][1] in atomic_counter:
                id = atomic_counter.index(queries[i][1])
                #print(atomic_index[id])
                a[res[id]:res[id]+queries[id][1]] =[0]* (id+queries[id][1]-id)
                res.append(atomic_index[id])
            else:
                res.append(-1)
    print("Final o/p: - ",res)

            #print(res[id],queries[id][1])



if __name__ == '__main__':
    memoryAllocator([0,1,0,0,0,1,1,0,0,0,1,0,0],[[0,2],[0,1],[0,1],[1,2],[1,4],[0,4]])
    memoryAllocator([0,0,0,0],[[0,4],[0,1],[1,1],[0,2],[0,2]])
    memoryAllocator([1],[[0,1],[1,1]])
