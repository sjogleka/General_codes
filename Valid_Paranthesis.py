s = input()

'''while "()" in s or "{}" in s or '[]' in s:
    print("in while")
    s = s.replace("()", "").replace('{}', "").replace('[]', "")
if s == "":
    print("True")
else:
    print("False")
'''

for i in range(len(s)):
    #print("in while")
    s = s.replace("()", "").replace('{}', "").replace('[]', "")
if s == "":
    print("True")
else:
    print("False")

#print(isValid("{([()])}"))



