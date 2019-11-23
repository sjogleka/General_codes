from collections import Counter
#a = [1,3,2,2,3]
#a = [5,4,5,3,2]
#a = [2,2,2]
a = [2,1,2]

#q = [1,2,3,4,5]
#q = [1,2,3]
q = [1,2,3]
res = []
print(len(a))
#occurrencesInSubarraysSumedh(a,m)
for i in range(len(q)):
    most_common, num_most_common = Counter(a[q[i]-1:]).most_common(1)[0]
    res.append(num_most_common)

print(res)



