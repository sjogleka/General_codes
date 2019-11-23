#s = "amazing"
#pattern = "010"
s = "codesignal"
pattern  = "100"
s = list(s)
vowel = ['a','e','i','o','u','y']
def occurrences(string, sub):
    count = start = 0
    while True:
        start = string.find(sub, start) + 1
        if start > 0:
            count+=1
        else:
            return count
for i in range(len(s)):
    if s[i] in vowel:
        s[i] = "0"
    else:
        s[i]="1"
s =''.join(map(str, s))
print(s,pattern)
print(occurrences(s,pattern))

