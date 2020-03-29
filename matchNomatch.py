from collections import deque
class mathNomatch:
    def __init__(self,pattern):
        self.pattern = deque()
        self.pattern = pattern
        self.q = []
        self.patternLen = len(self.pattern)

    def match(self,ip):
        if len(self.q)<len(self.pattern):
            self.q.append(ip)
        else:
            self.q.pop(0)
            self.q.append(ip)

        #print(self.pattern,self.q,type(self.q))
        if self.q == self.pattern:
            return  "Match Found"
        else:
            return "No Match"

if __name__ == '__main__':
    s1 = mathNomatch([True,True,False,True])
    s2 = mathNomatch([True,False, True, True])
    while True:
        ip1 = input()
        if ip1.lower() == "true":
            print("... Calling s1 ....")
            print(s1.match(True))
            print("... Calling s2 ....")
            print(s2.match(True))
        else:
            print("... Calling s1 ....")
            print(s1.match(False))
            print("... Calling s2 ....")
            print(s2.match(False))






