import copy
a = [1,2,3,4,5,6,7]
#print(id(a),a)
############# Pass by Reference ############
print("................Pass by Reference..............")
def updateList(list1):
    list2 = list1
    list2 += [10]
n = [5, 6]
print(id(n))                  # 140312184155336
updateList(n)
print(n)                      # [5, 6, 10]
print(id(n))                  # 140312184155336

############# Pass by Value ############
print("................Pass by Value..............")
def updateNumber(n):
    n += 10
b = 5
print(id(b))                   # 10055680
updateNumber(b)                # 10055680
print(b)

########### Tuple ##########
##### Tuples are IMUTABLE #####
##### The “value” of an immutable object can’t change, but it’s constituent objects can #####
print("................ Tuple ..............")
a = [1,2,3]
x = "Sumedh"
t = (x,a)
print(t)
a.append(4)
print(t)















####### References ########
#https://medium.com/@meghamohan/mutable-and-immutable-side-of-python-c2145cf72747