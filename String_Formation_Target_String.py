from collections import OrderedDict
import itertools
def numWays(words, target):
    count = 0
    x = []
    target = list(target)
    d = OrderedDict()
    dictOrder = OrderedDict()
    for i in range(len(words)):
        temp = list(words[i])
        for j in range(len(temp)):
            if temp[j] in target:
                if temp[j] not in d:
                    d[temp[j]] = []
                d[temp[j]].append(j)
    for i in target:
        if i not in d:
            return 0
        else:
            dictOrder[i] = d[i]
    del(d)
    for i in dictOrder:
        x.append(dictOrder[i])
    res = list(itertools.product(*x))
    for i in res:
        if len(set(i))== len(target) and list(i) == sorted(i):
            count += 1
    return count


if __name__ == '__main__':
    count = 0
    # x = ["adc","aec","efg"]
    # x = ["valya","lyglb","vldoh"]
    x = ["xzu", "dfw", "eor", "mat", "jyc"]
    # target = "ac"
    # target = "val"
    target = "cf"


    print(numWays(x,target))


