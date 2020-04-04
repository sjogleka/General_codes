def maxActiveThread(intervals):
    d = {}

    for start,end in intervals:
        if start not in d:
            d[start] = 0
        if end not in d:
            d[end] = 0

        d[start]+=1
        d[end]-=1

    print(d)
    total_thread,max_thread =0,0
    for i in sorted(d.keys()):
        total_thread += d[i]
        max_thread = max(max_thread,total_thread)

    print(max_thread)

if __name__ == '__main__':
    maxActiveThread([[2,4],[3,5],[1,4],[5,7]])



