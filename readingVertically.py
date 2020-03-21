from collections import defaultdict
arr= ["Daisy","Rose","Hyacinth","Poppy"]
d= defaultdict(list)
res =""
for i in range(len(arr)):
    for j in range(len(arr[i])):
        d[j].append(arr[i][j])
for k,v in d.items():
    for elements in range(len(v)):
        res+=v[elements]
print(res)
