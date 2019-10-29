import math
import os
import random
import re
import sys

#path = []


def findBestPath(n, m, max_t, beauty, u, v, t):
    path = [[] for i in range(m)]
    for i in range(m-1):
        path[u[i]].append([v[i], t[i]])
        #print(i,n,m,u,v,t)
        path[v[i]].append([u[i], t[i]])

    return [0, 1]


if __name__ == '__main__':

    n = int(input().strip())

    m = int(input().strip())

    max_t = int(input().strip())

    beauty_count = int(input().strip())

    beauty = []

    for _ in range(beauty_count):
        beauty_item = int(input().strip())
        beauty.append(beauty_item)

    u_count = int(input().strip())

    u = []

    for _ in range(u_count):
        u_item = int(input().strip())
        u.append(u_item)

    v_count = int(input().strip())

    v = []

    for _ in range(v_count):
        v_item = int(input().strip())
        v.append(v_item)

    t_count = int(input().strip())

    t = []

    for _ in range(t_count):
        t_item = int(input().strip())
        t.append(t_item)

    result = findBestPath(n, m, max_t, beauty, u, v, t)

    print(str(result) + '\n')