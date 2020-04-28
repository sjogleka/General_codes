# Ref Link: - https://www.careercup.com/question?id=5633477589336064

class HotelId:
    def __init__(self,hotelId,username,uid,rating):
        self.hotelId = hotelId
        self.username = username
        self.uid = uid
        self.rating = rating

'''
class User:
    def __init__(self,username,uid):
        self.userName = username
        self.id = uid

    def getUserID(self):
        return self.id
'''

def function(l1):
    d = {}
    for i in range(len(l1)):
        if l1[i][0] not in d:
            d[l1[i][0]] = [0,0]
        d[l1[i][0]][0]+=l1[i][2]
        d[l1[i][0]][1]+=1

    return d

def function2(l2):
    d = {}
    for i in range(len(l2)):
        if l2[i].hotelId not in d:
            d[l2[i].hotelId] = [0,0]
        d[l2[i].hotelId][0]+=l2[i].rating
        d[l2[i].hotelId][1]+=1

    return d

def minAvg(data,avg):
    res= []
    for k,v in data.items():
        if v[0]/v[1]>=avg:
            res.append(k)
    return res

if __name__ == '__main__':
    #[[hotelID,userID,Rating]]
    l1 = [[3,1,7],[1,2,5],[2,1,4],[3,2,8],[1,1,8],[2,2,7]]
    data  = function(l1)
    print('Hotel IDs: - ',minAvg(data,6))

    # Follow-up
    rating1 = HotelId(3,'sumedh',1,7)
    rating2 = HotelId(1, 'omkar', 2, 5)
    rating3 = HotelId(2, 'sumedh', 1, 4)
    rating4 = HotelId(3, 'omkar', 2, 8)
    rating5 = HotelId(1, 'sumedh', 1, 8)
    rating6 = HotelId(2, 'omkar', 2, 7)
    l2 = [rating1,rating2,rating3,rating4,rating5,rating6]
    data = function2(l2)
    print("Hotel IDs part 2: - ",minAvg(data,6))

'''
    u1 = User('sumedh',2)
    u3 = User('sumedhpj', 3)
    u3 = User('sumedhjog', 4)
'''