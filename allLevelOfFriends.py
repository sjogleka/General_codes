import copy
def allLevelFriends(dict,name):
    res = []
    initial= namesofConnections(dict,name)
    #res = res.append(copy.deepcopy(initial))
    #res = copy.deepcopy(initial)
    res.append(initial[:])
    s= set()
    #print(initial)
    flag = True
    print("Start of while")
    while flag:
        print("--")
        if len(initial)==0:
            break
        #print(initial)
        temp = namesofConnections(dict,initial[0])
        #print("Set: -",s)
        if initial[0] not in s:
            s.add(initial[0])
            if temp==None:
                break
            if name in temp:
                temp.remove(name)
            if len(temp)!=0:
                res.append(temp[:])
                #print("Res after insertion", res)
                initial.extend(temp)
            #print(temp)
            initial.remove(initial[0])
            #print("Intial after removing",initial)
        else:
            initial.remove(initial[0])
            if temp[0] in s:
                temp.remove(temp[0])


    print(res)

def namesofConnections(dict,name):
    if name not in dict:
        return None
    else:
        return dict[name]



if __name__ == '__main__':
    dict={"Bob":["Alice","Sandra","Eric"],
          "Sandra":["Bob","Don"],
          "Alice":["Bob"],
          "Eric":["Bob"],
          "Don":["Sandra","Tim"],
          "Tim":["Don"]
          }
    allLevelFriends(dict,"Bob")