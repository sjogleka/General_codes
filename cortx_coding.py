'''
import re
from random import randint
def function1(string):
    arr = string.split('}')
    print(arr)
    tempArr = []

    for i in range(len(arr)):
        tmp = []
        tmp.append(arr[i].split('{'))
        for ele in tmp:
            if ele !='':
                temp = re.sub(r'{','',arr[i]).strip()
                if temp != '':
                    tempArr.append(temp)
    print(tempArr)
    print(".......")
    #print(tmp)

    subsets= []
    for s in tempArr:
        if '|' in s:
            subsets.append(s.split('|'))
        else:
            subsets.append(s)
    print(subsets)
    option = ""
    for opts in subsets:
        option += opts[randint(0, len(opts) - 1)] + " "
    print(option.strip())

#testStrings = "{this {specific|particular} example|an example {like|such as} this}"
testStrings = "{I am|I'm} {working on|starting} this {online |}interview. I hope Cortx thinks I am {{very|extremely} qualified|great|awesome}{!|.}"
#function1("{this {specific|particular} example|an example {like|such as} this}")
function1(testStrings)
'''

from random import randint

def getRandomoption(string):
    sets = []
    for s in string.split('}'):
        x = s.strip()
        if x:
            sets.extend(x.split("{"))
    #print(s)
    subsets = []
    for s in sets:
        if s:
            if '|' in s:
                subsets.append(s.split('|'))
            else:
                subsets.append([s])

    option = ""
    for opts in subsets:
        option += opts[randint(0, len(opts) - 1)] + " "
    print(option.strip())
    return option.strip()


# testStrings = "{this {specific|particular} example|an example {like|such as} this}"
testStrings = "{I am|I'm} {working on|starting} this {online |}interview. I hope Cortx thinks I am {{very|extremely} qualified|great|awesome}{!|.}"
getRandomoption(testStrings)
