# URLify
def urlift(str1,length):
    str1 = str1[:length].replace(' ','%20')
    print(str1)


if __name__ == '__main__':
    str1 = "Mr John Smith    "
    length = 13
    urlift(str1,length)