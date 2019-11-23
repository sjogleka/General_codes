#a = [1,1,1,2,1,3,4]
count =0
a = [1,1,2,1,2,1,1]
#a= []
if len(a)==0:
    print("Not a good tuple")
for i in range(len(a)-2):
    s = set()
    print(a[i],a[i+1],a[i+2])
    s.add(a[i])
    s.add(a[i+1])
    s.add(a[i+2])
    if len(s)==2:
        count+=1
        print("Good Tuple")
    else:
        print("Not a good tuple")
print("Count :- ",count)