fruits = ['mango','guava','pinapple','pomegranate']

fruity = []
for f in fruits:
    fruity.append(f.capitalize())
    fruity.sort()
    #sorted(fruity)
    #print(' '.join(fruity))


l1 = ['Tom','Mott',1985,1986]
l2 = [6,7,8,3,5]
#print('l2[0]:',l1[1])

#a = [1,2,1,3,-1,1,2,2]
#a = [-2,-5,4,4,4,3,3,3]


from sys import stdin

def myFunc(a):
    d = {}
    for i in range(len(a)):
        if a[i] in d:
            d[a[i]] = d[a[i]] + 1
        else:
            d[a[i]] = 1
    max_num = max(d.values())
    temp = 100000
    print(d)
    for k, v in d.items():
        if d[k] == max_num and k < temp:
            temp = k
    print("Max Value is: -",temp)

array = []
for line in stdin:
    n = int(line)
    array.append(n)

myFunc(array)

#############################################################
######################### Round 2 ###########################
#############################################################


class classA:
  def __init__(self,x,y):
    self.a = x+y

x = classA(1,2)
y =getattr(x,'a')
setattr(x,'a',y+1)
print(x.a)





