import collections
'''
        adj = collections.defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                adj[word[:i] + '_' + word[i+1:]].append(word)
        #print(adj)
        visited = set()
        q = collections.deque([(beginWord, 1)])
        while q:
            word, k = q.popleft()
            if word == endWord:
                return k
            if word not in visited:
                visited.add(word)
                for i in range(len(word)):
                    neighbors = word[:i] + '_' + word[i+1:]
                    for neighbor in adj[neighbors]:
                        q.append((neighbor, k+1))
            print(q)
        return 0 
'''
def ladderLength(beginWord, endWord, wordList):
    d = collections.defaultdict(list)

    for word in wordList:
        for letter in range(len(word)):
            d[word[:letter]+'*'+word[letter+1:]].append(word)
    visisted = set()

    queue = collections.deque([(beginWord,1)])
    dummyqueue = []
    #print(queue.popleft())
    while queue:
        print("------------")
        word,level = queue.popleft()
        if word == endWord:
            return  level
        if word not in visisted:
            visisted.add(word)
            for i in range(len(word)):
                tempArr = word[:i]+'*'+word[i+1:]
                #print(tempArr)
                for element in d[tempArr]:
                    #print(queue,element,element in dummyqueue)
                    if element not  in visisted and element not in dummyqueue:
                        dummyqueue.append(element)
                        queue.append((element,level+1))

        print(queue)
    print(d)


print(ladderLength("hit","cog",["hot","dot","dog","lot","log","cog"]))

