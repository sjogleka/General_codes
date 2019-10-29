'''
def Solution(word):
    soln_set = []
    # i points to the first char and j to the last char.
    i, lenofWord = 0, len(word)
    count = 0
    for i in range(0, lenofWord-2):
        j = lenofWord
        # This would break once a word in that sequence is found which doesnt have ABC, starting from the end towards allows us to break sooner.
        while j > i:
            if checkABC(word[i:j]):
                count += 1
                j -= 1
            else:
                break

    print(count)
'''

def  Solution2(word):
    dict = {'A':[],'B':[],'C':[]}
    maxpos = []
    for i, ltr in enumerate(word):
        if ltr == 'A':
            dict['A'].append(i)
            maxpos.append(i)
        if ltr == 'B':
            dict['B'].append(i)
            maxpos.append(i)
        if ltr == 'C':
            dict['C'].append(i)
            maxpos.append(i)
    print(dict)
    print(max(maxpos))

'''
def findMin(dict):
    for i in range(0,2):
        #dict[0]







def checkABC(partWord):
    if 'A' in partWord and 'B' in partWord and 'C' in partWord:
        return True
    else:
        return False
'''

'''
Solution 2

def analyzeInvestments(s):
    count = 0
    for i in range(len(s)):
        a = False
        b = False
        c = False
        for j in range(i+1, len(s) + 1):
            if a or 'A' in s[i:j]:
                a = True
            if b or 'B' in s[i:j]:
                b = True
            if c or 'C' in s[i:j]:
                c = True
            if a and b and c:
                count = count + len(s) - j + 1
                break
    print(count)
'''
test = ["ABC", "ABCCBA", "PQACBA", "ABBCZBAC"]
Solution2("ABCACBA")
#analyzeInvestments("ABBCZBAC")