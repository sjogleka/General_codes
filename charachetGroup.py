def characterGroup(s):
    if not s:
        return
    i = 0
    res = []
    while i < (len(s)):
        if s[i] == '[':
            i+=1
            temp = ord(s[i])
            ch = s[i]
            while s[i] !=']':
                if ord(s[i])<temp:
                    temp = ord(s[i])
                    ch = s[i]
                i+=1
            res.append(ch)
        i += 1

    return "".join(res)

if __name__ == '__main__':
    ip = '[abc][zyx][e]'

    characterGroup(ip)
