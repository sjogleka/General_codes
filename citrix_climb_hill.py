a = [9,8,7,2,2,3]
b = a.copy()
cost = 0
cost1 = 0
print(max(a))
print(a.index(9))

for i in range(len(a)):
    if i != a.index(max(a)):
        cost = cost -a[i]

cost = cost + max(a)
for i in range(len(a)-1):
    if a[i+1]>a[i]:
        min(a[i],a[i+2])
        cost1 = cost1 + (min(a[i],a[i+2])+a[i])
print(cost1)