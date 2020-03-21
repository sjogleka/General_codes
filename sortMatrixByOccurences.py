from collections import defaultdict
a = [[1,4,-2],[-2,3,4],[3,1,3]]


count = {}
for i in range(len(a)):
    for j in range(len(a)):
        if a[i][j] not in count:
            count[a[i][j]] = 0
        count[a[i][j]] += 1
m = []
x = defaultdict(list)
for k, v in count.items():
    x[v].append(k)

for keys in sorted(x.keys()):
    inp = sorted(x[keys])
    for digits in inp:
        m.extend(digits for x in range(keys))
print(m)
t = 0
for k in range(len(a), 0, -1):
    j = k
    i = len(a) - 1
    while (j <= len(a) - 1):
        a[i][j] = m[t]
        t += 1
        i = i - 1
        j = j + 1
for k in range(len(a) - 1, -1, -1):
    i = k
    j = 0
    while (i >= 0):
        a[i][j] = m[t]
        t += 1
        i = i - 1
        j = j + 1

print(a)