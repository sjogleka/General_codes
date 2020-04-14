given = "pasword"
s = ["pwd","aso","swd","ord"]
d = {}
for k in range(len(s)):
    word = s[k]
    for i in range(len(word)):
        if word[i] not in d:
            d[word[i]]  = []
        for j in range(i+1,len(word)):
            d[word[i]].append(word[j])

d2 =  {}
for k in range(len(s)):
    word = s[k]
    for i in range(len(word)-1,-1,-1):
        if word[i] not in d2:
            d2[word[i]]  = []
        for j in range(i-1,-1,-1):
            d2[word[i]].append(word[j])



print(d)
print(d2)



