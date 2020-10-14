from collections import defaultdict
def mostImprovedStudent(students, scores):
    d = defaultdict(list)
    maxDiff = float('-inf')
    for i in range(len(scores)):
        #print(d,scores)
        if len(d[students[i]])==0 or scores[i]>d[students[i]][-1][0]:
            d[students[i]].append([scores[i],i])
        elif len(d[students[i]])<2 or (d[students[i]][0][0]>scores[i] and d[students[i]][-1][1]>i):
            d[students[i]][0][0] = scores[i]

    
    for k,v in d.items():
        if v[-1][0]-v[0][0]>maxDiff:
            maxDiff = v[-1][0]-v[0][0]

    print(maxDiff)
    return maxDiff

#students = ["Mary","Steve","Joe","Mary","Steve","Billy"]
#scores = [100,500,380,99,20,50]

#students = ["Mary","Mary","Mary","Mary","Mary"]
#scores = [50,20,40,100,10]

#students = ["Mary","Steve","Steve","Mary","Steve",]
#scores = [19,70,99,80,100]

students = ["Joe","Joe","Joe","Steven","Steven"]
scores = [100,50,100,25,50]
mostImprovedStudent(students,scores)


