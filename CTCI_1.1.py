# Is Unique

def is_unique(s):
    bitVector = []
    for i in range(256):
        bitVector.append(False)
    for char in s:
        print(ord(char))
        if bitVector[ord(char)] == True:
            return "Not Unique"
        else:
            bitVector[ord(char)] = True
    return "Unique String"

def is_unique_using_set(s):
    unique_char = set()
    for char in s:
        if char in unique_char:
            return "Not Unique"
        else:
            unique_char.add(char)
    print("Set :- ", unique_char)
    return "Unique String"

def using_sort(s):
    s = sorted(s)
    print("sorted string: - ",s)
    for char in range(len(s)-1):
        if s[char]==s[char+1]:
            return "Not Unique String"
    return "Unique String"



if __name__ == '__main__':
    s = "SumedhS"
    print(is_unique(s))
    print(is_unique_using_set(s))
    print(using_sort(s))

