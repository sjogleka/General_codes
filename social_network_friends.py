d = {}
#counts = [3,3,1,1,3,3,3,2,2,3,4,4,5,1,2,4,1,2,4,1,2,3]
counts = [5,5,5,3,3,1,1,2,2,1,2,1,2,3,5,5]
#counts = [1,1,1,1]
s = enumerate(counts)
import operator as op
s = sorted(s, key=op.itemgetter(1), reverse= True)
i = 0
while i < len(s):
    j = 0
    #print(s[i][1])
    while i < len(s) and j < s[i][1]:
        print(s[i][0],end=" ")
        #print(s[i][0])
        i+=1
        j+=1
    print()