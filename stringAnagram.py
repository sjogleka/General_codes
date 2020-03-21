def stringAnagram(str1,str2):
    d= {}
    for i in range(len(str1)):
        if str1[i] in d:
            d[str1[i]] +=1
        else:
            d[str1[i]] = 1

    print(d)
    for  i in range(len(str2)):
        if str2[i] in d and d[str2[i]] >0:
            d[str2[i]]-=1
        else:
            print(str2[i])
            print("Not Anagram")
            break

    return  sum(d.values())==0

if __name__ == '__main__':
    print(stringAnagram("listen","silent"))
    print(stringAnagram("triangle", "integral"))
