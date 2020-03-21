import re

def patterMatch(str1):
    result = re.findall('(?<=1)[0]+(?=1)', str1)

    print(result)



    '''
    result = re.findall(r'(10+1)',str1)
    start = 0
    s = set()
    end = len(str1)
    print(result)
    while True:
        result.append(re.findall(r'10+1',str1[start:end]))
        start+=1
        if start==end:
            break
    print(result)

    for i in range(len(result)):
        if result[i] not in s:
            s.add(result[i])

    print(s)
    '''





if __name__ == '__main__':
    patterMatch("1010001001000abc0011101")

    101
    10001
    1001
    101