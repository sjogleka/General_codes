# Check Permutation
from collections import Counter as c
def chkPermutation(str1,str2):
    if len(str1)!=len(str2):
        return False
    s = {}
    #s2 = c(str1)
    #print(s2)
    for char in str1:
        if char in s:
            s[char] +=1
        else:
            s[char]=1
    print("Before :-",s)
    for char in str2:
        if char not in s:
            print("After Removal: -", s)
            return False
        elif s[char]<=0:
            print("After Removal: -", s)
            return False
        else:
            s[char]-=1
    print("After Removal: -",s)
    return True

if __name__ == '__main__':
    str1 = "sumedha"
    str2 = "dhumess"

    print(chkPermutation(str1,str2))
