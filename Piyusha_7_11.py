# fruits = ['mango','guava','pinapple','pomegranate']
#
# fruity = []
# for f in fruits:
#     fruity.append(f.capitalize())
#     fruity.sort()
#     #sorted(fruity)
#     #print(' '.join(fruity))
#
#
# l1 = ['Tom','Mott',1985,1986]
# l2 = [6,7,8,3,5]
# #print('l2[0]:',l1[1])
#
# #a = [1,2,1,3,-1,1,2,2]
# #a = [-2,-5,4,4,4,3,3,3]
#
#
# from sys import stdin
#
# def myFunc(a):
#     d = {}
#     for i in range(len(a)):
#         if a[i] in d:
#             d[a[i]] = d[a[i]] + 1
#         else:
#             d[a[i]] = 1
#     max_num = max(d.values())
#     temp = 100000
#     print(d)
#     for k, v in d.items():
#         if d[k] == max_num and k < temp:
#             temp = k
#     print("Max Value is: -",temp)
#
# array = []
# for line in stdin:
#     n = int(line)
#     array.append(n)
#
# myFunc(array)
#
# #############################################################
# ######################### Round 2 ###########################
# #############################################################
#
#
# class classA:
#   def __init__(self,x,y):
#     self.a = x+y
#
# x = classA(1,2)
# y =getattr(x,'a')
# setattr(x,'a',y+1)
# print(x.a)
class Bucket:
    def __init__(self):
        self.bucket = []

    def get(self, key):
        for (k, v) in self.bucket:
            if k == key:
                return v
        return -1

    def update(self, key, value):
        found = False
        for i, kv in enumerate(self.bucket):
            if key == kv[0]:
                self.bucket[i] = (key, value)
                found = True
                break

        if not found:
            self.bucket.append((key, value))

        print(self.bucket)

    def remove(self, key):
        for i, kv in enumerate(self.bucket):
            if key == kv[0]:
                del self.bucket[i]


class MyHashMap(object):

    def __init__(self):
        self.key_space = 2069
        self.hash_table = [Bucket() for i in range(self.key_space)]


    def put(self, key, value):
        hash_key = key % self.key_space
        self.hash_table[hash_key].update(key, value)


    def get(self, key):
        hash_key = key % self.key_space
        return self.hash_table[hash_key].get(key)


    def remove(self, key):
        hash_key = key % self.key_space
        self.hash_table[hash_key].remove(key)


hashMap = MyHashMap()
hashMap.put(1, 1)
hashMap.put(2, 2)
print("hashMap.get(1)",hashMap.get(1))
print("hashMap.get(3)",hashMap.get(3))
hashMap.put(2070, 3)
hashMap.put(4139, 9)
print("hashMap.get(2070)",hashMap.get(2070))
