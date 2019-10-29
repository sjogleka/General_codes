def process(num):
    if len(num) != 8:
        return "INVALID"
    try:
        s = int(num[2:],16)
    except:
        return  "INVALID"
    sum =0
    while s!=0:
        sum+=int(s%10)
        s = s//10
    if hex(sum)[2:] == num[:2].lower():
        return "INVALID"
    else:
        "INVALID"

def process_2(line):
    if len(line) != 8:
        return "INVALID"
    try:
        a = int(line, 16)
    except:
        return "INVALID"
    try:
        s = int(line[2:], 16)
        x = int(line[:2], 16)
    except:
        return "INVALID A"
    sum = 0
    while(s > 0):
        sum = sum + s%10
        s = s//10
    if x == sum:
        return "VALID"
    return "INVALID"


print(process())