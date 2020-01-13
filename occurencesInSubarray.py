#----- Occurrences in Subarrays ------

from collections import Counter
def occurrencesInSubarrays_1(arr, m):
    res = []
    i = 0
    while i <= len(arr) - m:
        if (i+m <= len(arr)):
            most_common, num_most_common = Counter(arr[i:i+m]).most_common(1)[0]
            res.append(num_most_common)
        i += 1
    return res

def occurrencesInSubarrays(arr,m):
    res = []
    i = 0
    while i <= len(a) - m:
        lst = a[i:i + m]
        res.append(max(set(a[i:i + m]), key=lst.count))
        i += 1
    return res


#a = [1,3,2,2,3]
#a = [1,2]
a = [2,1,2,3,3,2,2,2,2,1]
#m = 2
m = 3
res = []
print(len(a))
print(occurrencesInSubarrays(a,m))
print(occurrencesInSubarrays_1(a,m))

