from collections import defaultdict
import datetime,math
class Solution:
    def __init__(self,string):
        self.string = string.split(',')
        self.city = defaultdict(list)
        self.maxEle = self.preProcessing()
        self.res = [0 for _ in range(self.maxEle)]
        self.mainCalculation()

    def preProcessing(self):
        i,j = 0,0
        while i<len(self.string):
            self.city[self.string[i+1].strip()].append([datetime.datetime.strptime(self.string[i+2].strip(),'%Y-%m-%d %H:%M:%S'),self.string[i].split('.')[1],j])
            i+=3
            j+=1
        return j

    def mainCalculation(self):
        for k,v in self.city.items():
            i = 1
            maxLeading = str(int(math.log(len(v))))
            self.city[k] = sorted(v,key=lambda m:m[0])
            for ele in self.city[k]:
                op = k+("{:0"+maxLeading+"d}").format(i)+"."+ele[1]
                i+=1
                self.res[ele[2]] = op

        print("\n".join(self.res))





if __name__ == '__main__':
    s = "photo.jpg, Warsaw, 2013-09-05 14:08:15," \
        "john.png, London, 2015-06-20 15:13:22," \
        "myFriends.png, Warsaw, 2013-09-05 14:07:13," \
        "Eiffel.jpg, Paris, 2015-07-23 08:03:02," \
        "pisatower.jpg, Paris, 2015-07-22 23:59:59," \
        "BOB.jpg, London, 2015-08-05 00:02:03," \
        "notredame.png, Paris, 2015-09-01 12:00:00," \
        "me.jpg, Warsaw, 2013-09-06 15:40:22," \
        "a.png, Warsaw, 2016-02-13 13:33:50," \
        "b.jpg, Warsaw, 2016-01-02 15:12:22," \
        "c.jpg, Warsaw, 2016-01-02 14:34:30," \
        "d.jpg, Warsaw, 2016-01-02 15:15:01," \
        "e.png, Warsaw, 2016-01-02 09:49:09," \
        "f.png, Warsaw, 2016-01-02 10:55:32," \
        "g.jpg, Warsaw, 2016-02-29 22:13:11"
    o1 = Solution(s)

    # print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    '''
    print("{:02d}".format(1))
    print("{:03d}".format(1))
    print("{:02d}".format(100))
    print("{:03d}".format(100))
    '''


