#s = "aaBabcDaA"
#s = "Codility"
#s = "cCaAvVzXZ"
s = "cCeEzZ"
res = ""
res1=-1
t =set()
#print(ord("a"),ord("A"))
for i in range(len(s)):
    t.add(ord(s[i]))

for i in range(len(s)):
    if ord(s[i])+32 in t and res1<ord(s[i]):
        res = s[i]
        res1 = ord(s[i])
if res:
    print(res)
else:
    print("NO")