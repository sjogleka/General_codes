pali = 'ada'

new_string = ""

replaced = False
#if len(pali)==3 and if pali[0]=='a'
for i, c in enumerate(pali):
    if not replaced:
        if c > 'a' and (len(pali)//2 != i or len(pali)%2 == 0):
            new_string += 'a'
            replaced = True
        else:
            new_string += c
    else:
        new_string += c


if new_string == pali:
    print ("IMPOSSIBLE")
else:
    print ("new non palindrome lexicographically smaller string:", new_string)