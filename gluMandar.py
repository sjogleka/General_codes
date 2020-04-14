'''

import collections
import datetime as d



data = [{"game_id":"Racing","user_id":"ABC123","amt":5,"date":"2020-01-01"},
        {"game_id":"Racing","user_id":"ABC123","amt":1,"date":"2020-01-04"},
        {"game_id":"Racing","user_id":"CDE123","amt":1,"date":"2020-01-04"},
        {"game_id":"DH","user_id":"CDE123","amt":100,"date":"2020-01-03"},
        {"game_id":"DH","user_id":"CDE456","amt":10,"date":"2020-01-02"},
        {"game_id":"DH","user_id":"CDE789","amt":5,"date":"2020-01-02"},
        {"game_id":"DH","user_id":"CDE456","amt":1,"date":"2020-01-03"},
        {"game_id":"DH","user_id":"CDE456","amt":1,"date":"2020-01-03"}]

no_of_players = collections.defaultdict(set)
cumulative_sum = collections.defaultdict(lambda: [0] * 4)
game_id = []

for i in range(len(data)):
    no_of_players[data[i]['game_id']].add(data[i]['user_id'])
#print(no_of_players)

dates = ["2020-01-01","2020-01-02","2020-01-03","2020-01-04"]
end_date = max(data, key=lambda r: r['date'])
print(end_date['date'])
end_date = d.datetime.strptime(end_date['date'], "%Y-%m-%d")
print(end_date)

for k,v in no_of_players.items():
    game_id.append(k)

for i in range(len(dates)):
    for j in range(len(data)):
        if data[j]['date'] == dates[i]:
            cumulative_sum[data[j]['game_id']][i] +=data[j]['amt']
#print(len(cumulative_sum))
for k,v in cumulative_sum.items():
    temp =v
    for j in range(1,len(temp)):
        temp[j] = temp[j-1]+temp[j]
    cumulative_sum[k] = temp
print(cumulative_sum)
print("Game    Age      Cum_rev     Total_unique_payers_per_game")
for k,v in cumulative_sum.items():
    for j in range(len(v)):
        print(k,"\t",j,"\t",v[j],"\t",len(no_of_players[k]))

'''


import collections
import datetime as d
data = [{"game_id":"Racing","user_id":"ABC123","amt":5,"date":"2020-01-01"},
        {"game_id":"Racing","user_id":"ABC123","amt":1,"date":"2020-01-04"},
        {"game_id":"Racing","user_id":"CDE123","amt":1,"date":"2020-01-04"},
        {"game_id":"DH","user_id":"CDE123","amt":100,"date":"2020-01-03"},
        {"game_id":"DH","user_id":"CDE456","amt":10,"date":"2020-01-02"},
        {"game_id":"DH","user_id":"CDE789","amt":5,"date":"2020-01-02"},
        {"game_id":"DH","user_id":"CDE456","amt":1,"date":"2020-01-03"},
        {"game_id":"DH","user_id":"CDE456","amt":1,"date":"2020-01-03"}]

class Cumulative:

    def __init__(self,data):
        self.data = data
        self.finalResult = list()

    def getRow(self,game, Age, Cum_rev, unique_players=0):
        d = {
            'game': game,
            'Age': Age,
            'Cum_Rev': Cum_rev,
            'Unique_Players': unique_players
        }
        return d

    def getAmt(self, game, date):
        amt = 0
        for i in self.data:
            if i['game_id'] == game and i['date'] == date:
                amt += i['amt']
        return amt

    def getUniquePlayers(self):
        no_of_players = collections.defaultdict(set)
        for i in self.data:
            no_of_players[i['game_id']].add(i['user_id'])
        return no_of_players

    def getCumulative(self):
        numberOfPlayers = self.getUniquePlayers()


        game = set()
        for i in data:
            game.add(i['game_id'])

        end_date = max(data, key=lambda r: r['date'])
        end_date = d.datetime.strptime(end_date['date'], "%Y-%m-%d")


        for g in game:
            start_date = d.datetime.strptime('2020-01-01', "%Y-%m-%d")
            age = 0
            cum_amt = 0
            while start_date <= end_date:
                amt = self.getAmt(game=g, date=start_date.strftime('%Y-%m-%d'))
                cum_amt += amt
                l = self.getRow(game=g, Age=age, Cum_rev=cum_amt, unique_players= len(numberOfPlayers[g]))
                age += 1
                self.finalResult.append(l)
                start_date += d.timedelta(days=1)
        return self.finalResult
c = Cumulative(data)
result = c.getCumulative()
print("Game    Age      Cum_rev     Total_unique_payers_per_game")
for ele in result:
    print(ele['game'],'\t',ele['Age'],'\t',ele['Cum_Rev'],'\t',ele['Unique_Players'])




