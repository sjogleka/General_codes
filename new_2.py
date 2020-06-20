from collections import Counter,defaultdict
def duplicatesOnSegment_1(arr):
    count = 0
    for i in range(len(arr)):
        n = i+1
        while n <= len(arr):
            sub = Counter(arr[i:n])
            flag = True
            for element in sub.values():
                if element<2:
                    flag = False
                    break
            if flag:
                count+=1
            n += 1

    return count

def duplicatesOnSegment_2(arr):
    def helper(arr, start, end, count):
        if end == len(arr):
            return count
        elif start > end:
            return helper(arr, 0, end + 1, count)
        else:
            sub = Counter(arr[start:end + 1])
            flag = True
            for element in sub.values():
                if element < 2:
                    flag = False
                    break
            if flag:
                count += 1
            return helper(arr, start + 1, end, count)

    return helper(arr,0,0,0)



def duplicatesOnSegment(arr):
    d = defaultdict(list)
    count = 0
    for idx,ele in enumerate(arr):
        d[ele].append(idx)

    for k,v in d.items():
        if len(v)>=2:
            for i in range(len(v)):
                j = i+1
                while j<len(v):
                    sub = Counter(arr[i:v[j]+1])
                    #print(arr[i:v[j]+1])
                    flag = True
                    for element in sub.values():
                        if element < 2:
                            flag = False
                            break
                    if flag:
                        count += 1
                    j+=1

    print(count)




    print(d)


if __name__ == '__main__':
    #arr = [1,2,1,2,3]
    arr = [0,0,0]
    #print(duplicatesOnSegment([1,2,1,2,3]))
    #print(duplicatesOnSegment([0,0,0]))
    #print(duplicatesOnSegment([0,1,1,1,11]))
    print(duplicatesOnSegment(arr))