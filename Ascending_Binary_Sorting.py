count_1 ={}
answer = []
a = [5,3,10,7,14]
for i in range(len(a)):
    m = bin(a[i])[2:].count('1')
    if m not in count_1:
        count_1[m] = []
    count_1[m].append(a[i])
for k in sorted(count_1.keys()):
    count_1[k].sort()
    for inp in count_1[k]:
        answer.append(inp)

print(answer)

