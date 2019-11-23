#----- Occurrences in Subarrays ------

from collections import Counter
def occurrencesInSubarrays(arr, n):
    res = []
    for i in range(len(arr)):
        if (i+n <= len(arr)):
            most_common, num_most_common = Counter(arr[i:i+n]).most_common(1)[0]
            res.append(num_most_common)

    return res


a = [1,3,2,2,3]
#a = [1,2]
#m = 2
m = 4
res = []
print(len(a))
i = 0
while i <= len(a)-m:
    lst = a[i:i+m]
    res.append(max(set(a[i:i+m]), key=lst.count))
    i+=1

print(res)