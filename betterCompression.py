def betterCompression(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    d = {}
    i = 0
    res  = ""
    if not s:
        return res
    while i<len(s):
        ch = s[i]
        if ch in alphabet:
            start = i+1
            end = start
            while end<len(s) and (s[end]>='0' and s[end]<='9'):
                end+=1
            if ch in d:
                d[ch]+=int(s[start:end])
            else:
                d[ch] = int(s[start:end])
            i = end
        else:
            i+=1

        print(d)

    d = sorted(d.items())
    print(d)
    for ele in d:
        res+=ele[0]+str(ele[1])
    print(res)
    return res


betterCompression("a12c56a1b5")
betterCompression("a1231456789b56c1a1")
#betterCompression("a12c56a1b5")

