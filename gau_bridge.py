from collections import defaultdict
def conflict(listA):
    d = defaultdict(list)
    visited  = set()
    res= []
    for i in range(len(listA)):
        if i in visited:
            continue
        start,end,tag = listA[i][0],listA[i][1],listA[i][2]
        for j in range(i+1,len(listA)):
            tempstart, tempend, temptag = listA[j][0], listA[j][1], listA[j][2]
            if tempstart<end:
                d[tag].append(temptag)
                end = tempend
                visited.add(j)
    #print(d)
    for k,v in d.items():
        temp = []
        temp.append(k)
        temp.extend(v)
        res.append(temp)
    print(res)

    return  res


if __name__ == '__main__':
    #ip = [[1,2,'a'],[2,5,'b'],[4,6,'c'],[5,7,'d'],[8,12,'e'],[11,15,'f']]
    ip = [[1, 2, 'a'], [2, 5, 'b'], [4, 6, 'c'], [5, 7, 'd'], [8, 12, 'e'], [11, 15, 'f'],[20,22,'g'],[21,24,'h']]
    dict  = conflict(ip)

