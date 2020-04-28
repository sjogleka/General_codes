
def giveLargest(a,b):
    if int(str(a)+str(b))> int(str(b)+str(a)):
        return int(str(a)+str(b))
    else:
        return int(str(b)+str(a))

def findelem(lista):
    while len(lista)!=1:
        lista.insert(0,giveLargest(lista.pop(0),lista.pop(0)))
    print(lista)

if __name__ == '__main__':
    ip = [3,30,34,5,9]
    #ip = [10, 2]
    #ip = [0,9,8,7,6,5,4,3,2,1]
    findelem(ip)