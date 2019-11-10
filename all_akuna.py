#------------Heta Akuna-------------------

#----------------Changed Sort----------------

def returnlarge(s,a):
    s = sorted(s)
    i=0
    try:
        while a >= s[i]:
            i+=1
    except:
        return None
    return s[i]
def returnsmall(s,a):
    s = sorted(s,reverse= True)
    i=0
    try:
        while a <= s[i]:
            i+=1
    except:
        return None
    return s[i]
def changedSort(s):
    s = list(s)
    res = []
    res.append(s.pop(s.index(min(s))))
    i = 0
    #print(s,res)
    while i < len(s):
        # print(i,len(s))
        x = returnlarge(s,res[-1])
        if x:
            res.append(s.pop(s.index(x)))
            i+=1
        else:
            break
    x = returnlarge(s, res[-1])
    if x:
        res.append(s.pop(s.index(x)))
    i=0
    while i < len(s):
        x = returnsmall(s[i:],res[-1])
        if x:
            res.append(s.pop(s.index(x)))
            i+=1
        else:
            break
    x = returnsmall(s, res[-1])
    if x:
        res.append(s.pop(s.index(x)))
    if s:
        res += s
    return ''.join(res)

# print(changedSort('aaazzz'))

#-------------Roman Names-----------------

import operator as op


def romanToInt(s):
    num = 0
    my_funcs = {
        'I': (lambda num: -1 if num >= 5 else 1),
        'V': (lambda num: 5),
        'X': (lambda num: -10 if num >= 50 else 10),
        'L': (lambda num: 50),
        'C': (lambda num: -100 if num >= 500 else 100),
        'D': (lambda num: 500),
        'M': (lambda num: 1000)
    }
    for el in reversed(list(s)):
        # print(el)
        num += my_funcs[el](num)

    return num
def sortRoman(names):
    res = []
    for i in names:
        res.append(i.split(' '))
    for i in range(len(res)):
        x = romanToInt(res[i][1])
        res[i].append(x)
    res = sorted(res, key= op.itemgetter(0,2))
    for i in range(len(res)):
        res[i].pop(-1)
        res[i] = ' '.join(res[i])
    return res



#print(sortRoman(['Philippe I','Philip II','Bill L','Bill IX','Bill V','Bill X']))


#----------------------Minimum Operations------------------------

def searchInsert(nums, target):
    i = 0
    if nums == []:
        return i
    if nums[-1] < target:
        return len(nums)
    while (nums[i] < target):
        i += 1
    return i

def minimumOperations(a):
    res = []
    i = 0
    count = 0
    while i < len(a):
        j = searchInsert(res,a[i])
        count += min(j-0, len(res) - j)*2 + 1
        # print(min(j-0, len(res) - j)*2 + 1)
        res.insert(j,a[i])
        i+=1
    print(res,count)
a = [2,5,6,10]
# minimumOperations(a)

class Queue1:
    def _init_(self):
        self.s1 = []
        self.s2 = []
    def put(self,n):
        while self.s1:
            self.s2.append(self.s1.pop())

        self.s1.append(n)

        while self.s2:
            self.s1.append(self.s2.pop())
    def get(self):
        if self.s1:
            return self.s1.pop()
        return None

import queue as q
class Fifo:
    def _init_(self,size):
        self.fifo = q.Queue(size)
        self.cache = dict()

    def put(self,key, value):
        if self.fifo.full():
            self.cache.pop(self.fifo.get())

        self.fifo.put(key)
        self.cache[key] = value

    def get(self, key):
        try:
            return self.cache[key]
        except:
            return None

# fifo = Fifo(3)
# fifo.put(1,5)
# fifo.put(2,6)
# fifo.put(3,7)
# print(fifo.get(2))
# fifo.put(4,7)
# fifo.put(5,1)
# print(fifo.get(4))
# print(fifo.get(2))
# print(list(fifo.fifo.queue))
# print(fifo.cache)
# x = ['10','1','2','11']
# import heapq as hq
# print(hq.nsmallest(2,x))

# def listMax(n,operations):
#     x = [0]*n
#     for i in operations:
#         for j in range(i[0]-1,i[1]):
#             x[j] += i[2]
#     print(max(x))


def create(n):
    size = 1
    while n >= size:
        size *= 2
    return [0] * size


def range_add(fwam, fwaa, low, high, val):
    _update(fwam, fwaa, low, val, -val * (low - 1))
    _update(fwam, fwaa, high, -val, val * high)


def _update(fwam, fwaa, at, m, a):
    s = len(fwam)
    while at < s:
        fwam[at] += m
        fwaa[at] += a
        at += at & (-at)


def range_query(fwam, fwaa, at):
    m, a, st = 0, 0, at
    while at > 0:
        m += fwam[at]
        a += fwaa[at]
        at -= at & (-at)

    return m * st + a


def listMax(n, operations):
    fwam, fwaa = create(n), create(n)
    for a, b, k in operations:
        range_add(fwam, fwaa, a, b, k)

    best, prev = 0, 0
    for i in range(1, n + 1):
        curr = range_query(fwam, fwaa, i)
        best = max(best, curr - prev)
        prev = curr
    print(best)
    return best

# listMax(4,[
#         [2,3,603],
#         [1,1,286],
#         [4,4,882]
#         ])

# a = 'abpqrspqrs'
# minLen, maxLen = 2,4
# x = []
# for i in range(len(a)):
#     if i+maxLen > len(a):
#         break
#     j = i+minLen
#     while j < len(a) and j < i+maxLen+1:
#         x.append(a[i:j])
#         j+=1
#
# print(x)

#--------------Akuna 2-----------------
def wall():
    wallposition = [1,2,4,7]
    wallheight = [4,5,7,11]
    total_wallheight = [0]*max(wallposition)
    j=0
    for i in wallposition:
        total_wallheight[i-1] = wallheight[j]
        j+=1
    x = total_wallheight.copy()
    max_mud_length = -1
    for i in range(1,len(total_wallheight)-1):
        if total_wallheight[i] == 0:
            if total_wallheight[i+1] == 0:
                total_wallheight[i] = total_wallheight[i-1] + 1
                #max_mud_length = max(max_mud_length,total_wallheight[i])
            else:
                total_wallheight[i] = min(total_wallheight[i-1],total_wallheight[i+1])+1
                #max_mud_length = max(max_mud_length, total_wallheight[i])
    print(total_wallheight)
    total_wallheight1 = total_wallheight.copy()
    total_wallheight = x.copy()
    i = len(total_wallheight) - 1
    while i > 0:
        if total_wallheight[i] == 0:
            if total_wallheight[i-1] == 0:
                total_wallheight[i] = total_wallheight[i+1] + 1
                #max_mud_length = max(max_mud_length,total_wallheight[i])
            else:
                total_wallheight[i] = min(total_wallheight[i-1],total_wallheight[i+1])+1
                #max_mud_length = max(max_mud_length, total_wallheight[i])
        i-=1
    for i in range(len(total_wallheight)):
        total_wallheight[i] = min(total_wallheight[i],total_wallheight1[i])
        if x[i] == 0:
            max_mud_length = max(max_mud_length,total_wallheight[i])
    print(total_wallheight)
    print(x)
    print(max_mud_length)

import operator as op
def rearrange(elements):
    bin_array = []
    for i in elements:
        x = (i,bin(i).replace('0b','').count('1'))
        bin_array.append(x)
    bin_array.sort(key=op.itemgetter(1,0))
    a=[]
    for i in bin_array:
        a.append(i[0])
    return a
rearrange([5,3,7,10,14])

def getUnallottedUsers1(bids, totalShares):
    price_dict = dict()
    for i in bids:
        if i[2] not in price_dict:
            price_dict[i[2]] = [[i[0],i[1],i[3]]]
        else:
            price_dict[i[2]].append([i[0],i[1],i[3]])
    for i in price_dict:
        price_dict[i] = sorted(price_dict[i],key= op.itemgetter(2))
    while totalShares > 0:
        max_price = max(price_dict.keys())
        if len(price_dict[max_price]) == 1:
            totalShares -= price_dict[max_price][1]
            price_dict.pop(max_price)
        else:
            if (totalShares // len(price_dict[max_price])) > 0:
                x = totalShares // len(price_dict[max_price])
                for i in price_dict[max_price]:
                    i[1] -= x
                    totalShares -= x
                y = totalShares % len(price_dict[max_price])
                i = 0
                while y > 0 and i<len(price_dict[max_price]):
                    if price_dict[max_price][i][1] == 0:
                        i+=1
                        continue
                    price_dict[max_price][i][1] -= 1
                    totalShares -= 1
                    i+=1
                    y-=1
            else:
                y = totalShares % len(price_dict[max_price])
                i = 0
                while y > 0 and i < len(price_dict[max_price]):
                    if price_dict[max_price][i][1] == 0:
                        i += 1
                        continue
                    price_dict[max_price][i][1] -= 1
                    totalShares -= 1
                    i += 1
                    y -= 1
    return price_dict



# print(getUnallottedUsers([
#     [1,5,5,0],
#     [2,7,8,1],
#     [3,7,5,1],
#     [4,10,3,3]
# ], 18))

import math


def findCombination(n, min, max):
    result = 0
    m = {}

    for i in range(min, max):
        for j in range(min, max):
            if math.gcd(i, j) == 1:
                if m.get(i):
                    m[i] += 1
                else:
                    m[i] = 1

    for i in m:
        result += i ** (n - 1)

    return result

#print(findCombination(2,1,3))

def getUnallottedUsers(bids, totalShares):
    price_dict = dict()
    output = []
    for i in bids:
        if i[2] not in price_dict:
            price_dict[i[2]] = [[i[0], i[1], i[3]]]
        else:
            price_dict[i[2]].append([i[0], i[1], i[3]])
    for i in price_dict:
        price_dict[i] = sorted(price_dict[i], key=op.itemgetter(2))
    while totalShares > 0:
        max_price = max(price_dict.keys())
        if len(price_dict[max_price]) == 1:
            print(price_dict)
            print(price_dict[max_price])
            totalShares -= price_dict[max_price][0][1]
            price_dict.pop(max_price)
        else:
            if (totalShares // len(price_dict[max_price])) > 0:
                x = totalShares // len(price_dict[max_price])
                for i in price_dict[max_price]:
                    i[1] -= x
                    totalShares -= x
                y = totalShares % len(price_dict[max_price])
                i = 0
                while y > 0 and i < len(price_dict[max_price]):
                    if price_dict[max_price][i][1] == 0:
                        i += 1
                        continue
                    price_dict[max_price][i][1] -= 1
                    totalShares -= 1
                    i += 1
                    y -= 1
            else:
                y = totalShares % len(price_dict[max_price])
                i = 0
                while y > 0 and i < len(price_dict[max_price]):
                    price_dict[max_price][i][1] -= 1
                    totalShares -= 1
                    i += 1
                    y -= 1
                for j in range(i, len(price_dict[max_price]) - 1):
                    output.append(price_dict[max_price][i][0])

            price_dict.pop(max_price)

    for key in price_dict:
        for i in range(0, len(price_dict[key])):
            output.append(price_dict[key][i][0])

    return output


# print(getUnallottedUsers([
#     [1, 5, 5, 0],
#     [2, 7, 8, 1],
#     [3, 7, 5, 1],
#     [4, 10, 3, 3]
# ], 18))

from datetime import datetime
class HashTable:
    def _init_(self, rawEvents):
        self.hwm = datetime.utcfromtimestamp(0)
        self.hashtable = dict()
        for i in rawEvents:
            query = i.split('|')
            self.operate_HT(query)

    def operate_HT(self,query):
        if query[1] == 'INSERT':
            self.insert(query[2],query[3])
        elif query[1] == 'UPSERT':
            self.upsert(query[2], query[3])
        elif query[1] == 'DELETE':
            self.delete(query[2])
        x = int(query[0])/1000
        self.hwm = datetime.utcfromtimestamp(x)

    def insert(self,key,value):
        if key not in self.hashtable:
            self.hashtable[key] = value
    def upsert(self,key, value):
        self.hashtable[key] = value

    def delete(self,key):
        if key in self.hashtable:
            self.hashtable.pop(key)
    def table(self):
        return self.hashtable

    def high_watermark(self):
        return self.hwm

# h = HashTable([
#     '1563454984001|INSERT|test|123',
#     '1563454984002|UPSERT|test|123',
#     '1563454984003|DELETE|test'])
# print(h.table())
# print(h.high_watermark())
import codecs
def Akuna_12(s):
    a = []
    a.append(str(int(s[:16],16)))
    if int(s[16:18],16) == 0:
        a.append("INSERT")
    elif int(s[16:18],16) == 1:
        a.append("UPSERT")
    if int(s[16:18],16) == 2:
        a.append("DELETE")
    key_length = int(s[18:22],16)
    key_length = (key_length*2)
    key_value = codecs.decode(s[22:22+key_length],"hex")
    key_value = str(key_value)
    key_value = key_value.replace("b'",'')
    key_value = key_value.replace("'","")
    a.append(key_value)
    # value_length = int(s[22 + key_length:22+ key_length+4],16)
    value_length = 22+ key_length+4
    value_value = str(codecs.decode(s[value_length:],"hex"))
    value_value = value_value.replace("b'",'')
    value_value = value_value.replace("'","")
    a.append(value_value)
    return a
s = '0000016c052dcf4101000d746573745f6b65795f313233340012746573745f76616c75655f31323339393038'

def bytes_to_int(bytes):
    result = 0
    for b in bytes:
        result = result * 256 + int(b)
    return result
def someFunc():
    a = b'\x00\x00\x01l\x05-\xcfA\x00\x00\x0etest_key_09812\x00\x10test_value 12876'
    res = []
    #st = '\x00\x00\x01l\x05-\xcfA\x00\x00\x0etest_key_09812\x00\x10test_value 12876'
    epoch = bytes_to_int(a[:8])
    res.append(str(epoch))
    msg_id = bytes_to_int(a[8:9])
    msg_id = bytes_to_int(a[8:9])
    if msg_id == 0:
        res.append("INSERT")
    elif msg_id == 1:
        res.append("UPSERT")
    if msg_id == 2:
        res.append("DELETE")
    key_length = bytes_to_int(a[9:11])
    #res.append(key_length)
    key_value = a[11:11+key_length].decode('utf-8')
    res.append(key_value)
    value_length = bytes_to_int(a[25:27])
    #res.append(value_length)
    value_string = a[27:43].decode('utf-8')
    res.append(value_string)
    print(res)
    x= '|'.join(res)
    print(x)

#-----------------------Medha Akuna--------------------------

class PathCalculator:
    distance = {}  # dictionary that maintains distance between cities

    def process(self, line: str) -> str:

        possible_route = {}  # dictianery that maintains distance if there is possibility of two ticket route

        city1, city2, dis = list(line.split(':'))
        if not city1 in self.distance:  # Updating distance with respect to city1
            self.distance[city1] = {}
        self.distance[city1][city2] = int(dis)

        if not city2 in self.distance:  # Upadting distance with respect to city2
            self.distance[city2] = {}
        self.distance[city2][city1] = int(dis)

        for start_city in self.distance:  # Checking two ticket distance for each city
            d = self.distance[start_city]
            inter_city = max(d.keys(), key=(lambda k: d[k]))
            d = self.distance[inter_city]
            final_city = max(d.keys(), key=(lambda k: d[k]))
            if start_city != final_city:
                total_dis = self.distance[start_city][inter_city] + self.distance[inter_city][final_city]
                if start_city > final_city:
                    start_city, final_city = final_city, start_city
                if possible_route.get(total_dis):
                    if possible_route[total_dis] > (start_city, inter_city, final_city):
                        possible_route[total_dis] = (start_city, inter_city, final_city)
                else:
                    possible_route[total_dis] = (start_city, inter_city, final_city)
        print(self.distance)
        print(possible_route)
        if possible_route == {}:
            return "NONE"
        else:
            max_dis = max(possible_route)
            c1, c2, c3 = possible_route[max_dis]
            return ':'.join([str(max_dis),c1,c2,c3])
# ob=PathCalculator()
# l1='AAA:NYC:200'
# l2='CHI:AUS:200'
# l3='NYC:AUS:1000'
# l4='NYC:HAWAII:4393'
# l5='CHI:AUS:719'
# l6='AUS:LA:2414'
# print(ob.process(l1))
# print(ob.process(l2))
# print(ob.process(l3))
# print(ob.process(l4))
# print(ob.process(l5))
# print(ob.process(l6))

# ob=PathCalculator()
# l1='CHI:NYC:719'
# l2='NYC:LA:2414'
# l3='NYC:SEATTLE:2448'
# l4='NYC:HAWAII:4924'
# ob.process(l1)
# ob.process(l2)
# ob.process(l3)
# ob.process(l4)

# def prefixString(a,b):
#     pString = [a[0]]
#     for i in range(1,len(a)):