class Iterator():
    def __init__(self,lists):
        self.lists = lists
        self.arr = [0 for _ in range(len(lists))]
        self.listIndex = 0

    def getNextMin(self):
        currMin = float('inf')
        for i in range(len(self.arr)):
            #print("Accessing index: -",i)
            if self.arr[i]<len(self.lists[i]) and self.lists[i][self.arr[i]]<currMin:
                #print("...............")
                #print(self.lists[self.arr[i]],i, self.arr)
                currMin = self.lists[i][self.arr[i]]
                self.listIndex = i

        #print(self.listIndex,self.currMin)
        if self.arr[self.listIndex]>len(self.lists[self.listIndex]):
            print("Couldn't find small element")
        else:
            self.arr[self.listIndex] += 1



        return currMin



    def getNext(self):
        print("##### Output :-",self.getNextMin())
        #print("Now self.arr: -",self.arr)

if __name__ == '__main__':
    list1 = [[1,5,10],[2,4,9,100002],[0,3,1000]]
    it1 = Iterator(list1)

    it1.getNext()
    it1.getNext()
    it1.getNext()
    it1.getNext()
    it1.getNext()
    it1.getNext()
    it1.getNext()
    it1.getNext()
    it1.getNext()
    it1.getNext()
    it1.getNext()





