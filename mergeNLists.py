if __name__ == '__main__':
    l  = [[1,2,3],[3,4,5],[7,8,9],[1,2,3]]
    res = []
    finalOp = []
    l1 = l.pop(0)
    l2 = l.pop(0)
    for i in range(len(l1)):
        for j in range(len(l2)):
            res.append([l1[i],l2[j]])

    while len(l)>0:
        num = l.pop(0)
        curr_len = len(res)
        for i in range(curr_len):
            temp = res.pop(0)
            for j in range(len(num)):
                res.append(temp+[num[j]])


    print(res)
    print([1,3,7,3] in res)
    print([1,4,7,1] in res)
    print([3,4,9,2] in res)
    print([3,5,8,1] in res)











