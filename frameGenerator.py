def frameGenerator(n):
    res = []
    for i in range(1, n + 1):
        s = []
        for j in range(1, n + 1):
            if (i == 1 or i == n or j == 1 or j == n):
                #print("*",end="")
                s.append("*")
            else:
                #print(" ", end="")
                s.append(" ")

 #      print("".join(s))
        res.append("".join(s))
    return res

print(frameGenerator(8))