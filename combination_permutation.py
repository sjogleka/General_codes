#import os
import gc
from itertools import permutations
import itertools

def arraysCount(n,m,totalcost):
    idx = 0
    result = []
    while idx < len(n):
        print('answers index: ',idx)
        temp_result = []

        if n[idx] <= m[idx]:
            all_arrays = perm(n[idx],m[idx])
            print('all_arrays:',all_arrays)
        else:
            all_arrays = perm_rep(n[idx],m[idx])
            print('im here')
            print('all_arrays:', all_arrays)

        for each in all_arrays:
            if fun_totalCost(each) == totalcost[idx]:
                temp_result.append(each)
        result.append(len(temp_result))
        del(temp_result)
        gc.collect()
        idx += 1
    return result
    #print(result)


def fun_totalCost(element):
    curr_max = element[0]
    total_cost = 0

    for i in range(1,len(element)):
        if element[i] > curr_max:
            curr_max = element[i]
            total_cost += 1

    return total_cost

def perm(n,m):

    arr= []
    for i in range(1,m+1):
        arr.append(i)
    main_list = []
    for subset in permutations(arr, n):
        main_list.append(list(subset))
    return main_list

def perm_rep(n,m):
    arr = []
    for i in range(1, m + 1):
        arr.append(i)
    main_list = [list(p) for p in itertools.product(arr, repeat=n)]
    return main_list

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    '''
    n_count = int(input().strip())

    n =[]

    for i in range(n_count):
        n_item = int(input().strip())
        n.append(n_item)


    m_count = int(input().strip())

    m =[]

    for i in range(m_count):
        m_item = int(input().strip())
        m.append(m_item)

    totalCost_count = int(input().strip())

    totalCost =[]

    for i in range(n_count):
        totalCost_item = int(input().strip())
        totalCost.append(totalCost_item)

    '''

    res = arraysCount([2,3,4],[3,3,3],[1,2,3])
    #res = arraysCount(n,m,totalCost)
    print(res)
    #fptr.write('\n'.join(map(str,res)))
    #fptr.write('\n')

    #fptr.close()
#print("Result - ",res)

#print(perm_rep(4,3))
#[2,3,4],[3,3,3],[1,2,2]


