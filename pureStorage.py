def compute_number_score(n):
    n = str(n)
    points = (n.count('5'))*2
    for i in range(len(n)):
        if i+1 < len(n) and n[i] == '3' and n[i+1]=='3':
            points+=4
        if int(n[i]) % 2 == 1:
            points+=1
    if n[-1] == '5':
        points+=6
    #print(points)
    count = 1
    a = 0
    for i in range(1,len(n)):
        if int(n[i]) - int(n[i-1]) == 1:
            count+=1
        else:
            a+=count**2
            count = 1
    a+=count**2
    points += a
    return points

print(compute_number_score())