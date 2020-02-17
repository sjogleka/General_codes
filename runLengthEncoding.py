if __name__ == '__main__':
    x = "wwwwaaadexxxxxx"
    op = "w4a3d1e1x6"
    d = {}
    res = ""
    for i in range(len(x)):
        if x[i] in d.keys():
            d[x[i]]+=1
        else:
            d[x[i]] = 1
    print(d)

    for k,v in d.items():
        res+=k+str(v)

    print(res)


