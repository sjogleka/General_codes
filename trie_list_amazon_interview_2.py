import  timeit


def findSimple1(data,keyword):
    if keyword in data:
        return True
    else:
        return False

# Follow-up 1
def findInSet(data,keyword):
    if keyword in data:
        return True
    else:
        return False



# Follow-up 2
def createDS(givenList):
    trie = {}
    for word in givenList:
        node = trie
        for letter in word:
            if letter not in node:
                node[letter]  = {}
            node = node[letter]
        node['End'] = 'End'
    return trie


def search(data,keyword):
    for word in keyword:
        if word in data:
            data = data[word]
        else:
            return False
        #print(data)
    if 'End' in data:
        return True
    return False


if __name__ == '__main__':
    givenList = ["hi","hello","height","high","sample1","same","abc","xyz"]*100000+["sumedh"]
    keyword = "sumedh"

    start  = timeit.default_timer()
    op1 = findSimple1(givenList,keyword)
    print("Keyword is present - ",keyword) if op1 else print("Not Found!")
    stop = timeit.default_timer()
    print("Running Time 1 - ",stop - start)

    #Follow-up1
    print("............................................")
    temp = set(givenList)
    start = timeit.default_timer()
    op2 = findInSet(set(givenList),keyword)
    print("Keyword is present - ",keyword) if op2 else print("Not Found!")
    stop = timeit.default_timer()
    print("Running Time 2 - ", stop - start)

    #Follow-up2
    print("............................................")
    data  = createDS(givenList)
    start = timeit.default_timer()
    op = search(data,keyword)
    print("Keyword is present - ",keyword) if op else print("Not Found!")
    stop = timeit.default_timer()
    print("Running Time 3 - ", stop - start)



