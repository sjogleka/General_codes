def sumOfDigits(s):
    sum = 0
    for i in range(len(s)):
        sum += int(s[i])
    return sum;

def findSchedules(workHours, dayHours, pattern):
    x = ()
    if '?' in pattern:
        index = pattern.index('?')
        first = str(pattern[:index])
        last = str(pattern[index+1:len(pattern)])
        for i in range(dayHours+1):
            result = findSchedules(workHours, dayHours, first + str(i) + last)
            x = x + result;
            # print(result)
            # print(x)
    else:
        #Pattern has no Question mark,
        #So, just sum digits and check if it matches WorkHours
        #print(sumOfDigits(pattern),workHours)
        if(sumOfDigits(pattern) == workHours):
            x = x + (pattern,)
    return x
res = findSchedules(56,8,'???8???')
print(res)