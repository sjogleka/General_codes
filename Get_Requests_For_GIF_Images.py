def sumedh_sol(filepath):
    s  = set()
    with open(filepath) as fp:
       for cnt, line in enumerate(fp):
           l = line.split()
           if "200" in l[-2] or "200" in l[-1]  and "gif" in l[-4].lower() and l[5].split('"')[1]=='GET':
                   temp = l[-4].split('/')
                   s.add(temp[-1])
                   #print(s)
    fp.close()
    f = open("gifs_hosts_access_log_00.txt", "w")
    s = list(s)
    for i in range(len((s))-1):
        print(s[i])
        f.write((s[i])+"\n")
    print(s[len(s)-1])
    f.write(s[len(s)-1])
    f.close()


def sakshat_sol(filepath):
    res = set()
    with open(filepath) as fp:
        for s in fp:
            s = s.split('"')
            # print(s)
            c = s[-1].strip().split(' ')
            if '200' not in c:
                continue
            b = s[1].strip().split('/')
            # print(b)
            flag = False
            for i in b:
                if 'GET' in i:
                    flag = not flag
                if 'gif' in i or 'GIF' in i:
                    temp = i.split(' ')[0]
                    if flag:
                        res.add(temp)
                    break
    print(res)

if __name__ == '__main__':
    filepath = 'hosts_access_log_00.txt'
    sumedh_sol(filepath)
    #sakshat_sol(filepath)
