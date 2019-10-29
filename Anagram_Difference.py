
import collections
def anagram(a,b):
    count = 0
    if len(a) != len(b):
        return -1

    dic = collections.Counter(a)

    for i in b:
        if i in dic:
            if dic[i]:
                dic[i] -= 1
            else:
                count += 1
        else:
            count += 1
    return count
a = 'abc'
b = 'def'
x = ['a','jk','abb','mn','abc']
y = ['bb','kj','bbc','op','def']
print(anagram(a,b))
for i in range(len(x)):
    print(anagram(x[i],y[i]))
#print(anagram(x,y))