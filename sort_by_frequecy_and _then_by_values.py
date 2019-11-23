from collections import Counter
def perseus_sort(l):
    counter = Counter(l)
    return sorted(l, key=lambda x: (counter[x], x))


li = [3,1,2,2,4]
print(perseus_sort(li))