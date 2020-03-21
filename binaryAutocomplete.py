from collections import defaultdict
from operator import  itemgetter

def binaryAutocomplete(command):
    res= []
    res.append(0)
    for i in range(1,len(command)):
        #print("_________________________________")
        temp = command[i]
        latest = -1
        initialK = 0
        for j in range(i-1,-1,-1):
            flag = True
            k = 0
            l =0
            #print("Comparing: - ",i,j,command[i],command[j])
            while flag:
                #print(k,initialK)
                if k<len(command[j]) and l<len(command[i]) and command[j][k]==command[i][l]:
                    #print("------")
                    #print("Checking: - ",command[j][k], command[i][l])
                    k+=1
                    l+=1
                else:
                    flag = False
            #print(k,initialK)
            if k>initialK:
                initialK = k
                latest = j
                #print("k,InitiaK",k,initialK,"Index: - ", latest + 1)
        if latest==-1:
            res.append(i)
        else:
            res.append(latest+1)
    print(res)


class Trie:
    def __init__(self):
        self.d ={}
        self.index= []

class sol:
    def indexing(self,arr):
        print("----"*40)
        root = Trie()
        res=defaultdict(list)
        final = []

        for id,elem in enumerate(arr):
            trie = root
            level = 0
            for char in elem:
                level+=1
                if char not in trie.d:
                    trie.d[char] = Trie()
                #print(trie.d.items())
                #print(trie.index)
                trie = trie.d[char]
                trie.index.append((id,level))
                #trie.index.append((id,elem))

        originalRoot = root

        for elem in arr:
            root = originalRoot
            for j in elem:
                if root:
                    root = root.d.get(j)
                    if root:
                        res[elem].extend(root.index)


        for k,v in res.items():
            res[k] = sorted(list(set(v)),key=lambda x: (x[1],x[0]),reverse=True)

        for i in range(len(arr)):
            temp = res[arr[i]]
            flag = False
            for j in range(len(temp)):
                if temp[j][0]<i:
                    #print("Candidates: -",temp[j])
                    final.append(temp[j][0]+1)
                    flag = True
                    break
            if not flag:
                final.append(i)
        print(res)
        print("Final Output: -",final)




if __name__ == '__main__':
    #binaryAutocomplete(["000","1110","01","001","110","11"])
    #binaryAutocomplete(["100110","1001","1001111"])
    #binaryAutocomplete(["1","10","11010"])


    s = sol()
    s.indexing(["000","1110","01","001","110","11"])
    s.indexing(["100110","1001","1001111"])
    s.indexing(["1","10","11010"])

