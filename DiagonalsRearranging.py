import itertools
def get_rows(grid):
    return [[c for c in r] for r in grid]

def get_cols(grid):
    return zip(*grid)

def get_backward_diagonals(grid):
    b = [None] * (len(grid) - 1)
    grid = [b[i:] + r + b[:i] for i, r in enumerate(get_rows(grid))]
    return [[c for c in r if c is not None] for r in get_cols(grid)]

#a = [["b", "b"],["c","a"]]
a= [["a","c","a","b","b"],["c","b","a","c","b"],["a","a","e","c","b"],["b","b","d","a","g"],["a","b","e","b","a"]]
arr = (get_backward_diagonals(a))
N = len(a)
res= {}
for j in range(len(arr)):
    shape_list = arr[j]
    g = itertools.cycle(shape_list)
    temp = []
    for i in range(N):
        shape = next(g)
        temp.append(shape)
    temp = "".join(temp)

    res[j+1] = temp

import operator

sorted_x = sorted(res.items(), key=operator.itemgetter(1))
print([x[0] for x in sorted_x])
print([x[0] for x in sorted_x])