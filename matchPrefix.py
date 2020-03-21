def prefixMatching(arr, str1, k):
    if k > len(str1):
        return "Error"
    prefix = str1[:k]
    #print(prefix)
    count =0
    for i in range(len(arr)):
        if len(arr[i])>k and arr[i][:k] == prefix:
            count +=1
    return count

if __name__ == '__main__':
    str1 = ["abba", "abbb", "abbc", "abbd", "abaa", "abca"]
    str2= ["geeks","geeksforgeeks","forgeeks"]
    print(prefixMatching(str1,"abbg",3))
    print(prefixMatching(str1, "abg", 2))
    print(prefixMatching(str1, "xyz", 2))
    print(prefixMatching(str2, "geeks", 2))