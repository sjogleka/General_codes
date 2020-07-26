def majorityElement(arr,size):
    d = {}
    for i in range(len(arr)):
        if arr[i] not in d:
            d[arr[i]] = 0
        d[arr[i]] +=1
        if d[arr[i]]>size//2:
            return arr[i]

    return -1

if __name__ == '__main__':
    print(majorityElement([8,8,2,4,8],5))
    #print(majorityElement("8 8 2 4 8 ", 5))
    print(majorityElement([1,2,3], 3))