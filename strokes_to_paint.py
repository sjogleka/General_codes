n=int(input())
s=input()
if len(set(s))==1:
    print(1)
else:
    c=0
    for i in range(len(s)-1):
        if s[i]!=s[i+1]:
            c+=1
        else:
            continue

    print(c+1)
