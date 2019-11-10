
def getEventsOrder(team1, team2, events1, events2):
    # Write your code here
    football = list()
    football.append({"team": team1, "event": events1})
    football.append({"team": team2, "event": events2})

    game_details_list = list()
    original_event = list()
    event_priority = ['G', 'Y', 'R', 'S']

    for f in football:
        for event in f["event"]:
            original_event.append(f["team"] + " " + event)

            # split events string to get details
            pattern = re.compile("([a-zA-Z\s])(\d+)[+]?(\d).([G,Y,R,S])([a-zA-Z\s]*)")
            split_event = pattern.search(event)

            # create a list of format ["team name", "player name", "time", "extra time", "event", "second player name"]
            record = list()
            record.append(f["team"])  # team name
            if split_event:
                record.append(split_event.group(1).strip())  # player name
                record.append(int(split_event.group(2).strip()))  # time
                record.append(
                    int(split_event.group(3).strip()) if len(split_event.group(3).strip()) > 0 else 0)  # extra time
                record.append(event_priority.index(split_event.group(4).strip()))  # event
                record.append(split_event.group(5).strip())  # second player
            game_details_list.append(record)

    # sorting the list to return index position of the sorted list
    new_num_index_sorted = (sorted(range(len(game_details_list)),
                                   key=lambda k: (
                                       game_details_list[k][2],  # time
                                       game_details_list[k][3],  # extra time
                                       game_details_list[k][4],  # event
                                       game_details_list[k][0],  # team name
                                       game_details_list[k][1],  # player name
                                       game_details_list[k][5])))

    # based on the index position, fetching result from original event list and appending in answer
    answer = list()
    for i in new_num_index_sorted:
        answer.append(original_event[i])
    return answer
# team1 = 'ABC'
# team2 = 'CBA'
# events1 = ['Mo Sa 45+2 Y','A 13 G']
# events2 = ['D 23 S F', 'Z 46 G']
# print(getEventsOrder(team1,team2,events1,events2))
# print(getEventsOrder("nolh","nzrdrrc",["inmuucz jzbkica 70 Y","ton wfnt 10 S inmuucz jzbkica","ecya kqvqy 20 S fkfk fuiyb senmofw"],["mysior pqfcz bxlnpn 49 G","mysior pqfcz bxlnpn 18 G","enc otagavd oevfg 86 Y"]))
# def minNum(A,n):
#     previous_letter_status, no_of_unread_letters, no_of_unread_segments = 0, 0, 0
#     for i in range(0,n):
#         if A[i] == 1:
#             no_of_unread_letters += 1
#         if previous_letter_status == 0 and A[i] == 1:
#             no_of_unread_segments += 1
#
#         previous_letter_status = A[i]
#
#     no_of_operations = no_of_unread_letters + max(no_of_unread_segments-1,0)
#     print(no_of_operations)
# minNum([0,0],2)

# int findCombination(int n, int min, int max)
# {
# 	long result = 0;
# 	unordered_map<int, int> m;
# 	for (int i = min; i <= max; i++)
# 	{
# 		for (int j = min; j <= max; j++)
# 		{
# 			if (std::gcd(i, j) == 1)
# 				m[i]++;
# 		}
# 	}
# 	auto iter = m.begin();
# 	while (iter != m.end())
# 	{
# 		result += pow(iter->second, n - 1);
# 		iter++;
# 	}
# 	return result;
# }
# import math
# def findCombination(rotorCount,minRotorValue,maxRotorValue):
#     result = 0
#     map = dict()
#     for i in range(minRotorValue,maxRotorValue+1):
#         if i % 2 == 0:
#             flag = True
#         else:
#             flag = False
#         for j in range(minRotorValue,maxRotorValue+1):
#             if j % 2 == 0 and flag:
#                 continue
#             if math.gcd(i,j) == 1:
#                 if i in map:
#                     map[i] += 1
#                 else:
#                     map[i] = 1
#     print(map)
#     for i in map:
#         result += map[i] ** (rotorCount-1)
#     return result

# print(findCombination(3,2,6))
import networkx
from networkx import (
    draw,
    DiGraph,
    Graph,
)
# def minOperations(n,fro,to):
#     undirected = Graph()
#     undirected.add_edges_from(list(zip(fro, to)))
#     for i in range(1,n+1):
#         if i not in undirected.nodes():
#             undirected.add_node(i)
#     # print(undirected.nodes())
#     # draw(undirected, with_labels=True)
#     nCC = networkx.number_connected_components(undirected)
#     s = networkx.connected_components(undirected)
#     s = (list(s))
#     H = 0
#     for i in range(len(s)):
#         h = undirected.subgraph(list(s[i]))
#         H += (len(h.edges()) - len(s[i]) + 1)
#     if H >= nCC - 1:
#         print(nCC-1)
#     else:
#         print(-1)
# n = 4
# fro = [1,3]
# to = [2,4]

# # minOperations(n,fro,to)
# import operator as op
# def reduce_values(d):
#     for i in d:
#         d[i] -= 10
#     return d
# def minimum(s):
#     res = 0.0
#     gumDict = dict()
#     for i in s:
#         if i in gumDict:
#             gumDict[i] = 1000
#         else:
#             if len(gumDict) > 2:
#                 s = min(gumDict.items(), key=op.itemgetter(1))
#                 gumDict.pop(s[0])
#                 res += s[1]/100
#             gumDict[i] = 1000
#         gumDict = reduce_values(gumDict)
#     return float(round(res,1))
#
# minimum(['red','red'])








class PathCalculator:
    # You may enter code here.

    distance = {}  # dictionary that maintains distance between cities

    def process(self, line: str) -> str:
        if line == None:
            return "NONE"
        possible_route = {}
        flag1, flag2 = False, False
        city1, city2, dis = list(line.split(':'))
        if city1 not in self.distance:
            self.distance[city1] = {}
            flag1 = True
        self.distance[city1][city2] = int(dis)

        if city2 not in self.distance:
            self.distance[city2] = {}
            flag2 = True
        self.distance[city2][city1] = int(dis)
        if flag1 and flag2:
            return "NONE"
        for start_city in self.distance:
            d = self.distance[start_city]
            # print(d.keys())
            for inter_city in d:
                d1 = self.distance[inter_city]

                final_city = max(d1.keys(), key=(lambda k: d1[k]))
                if start_city != final_city and (inter_city in self.distance[start_city]):

                    total_dis = self.distance[start_city][inter_city] + self.distance[inter_city][final_city]
                    if start_city > final_city:
                        start_city, final_city = final_city, start_city
                    if total_dis in possible_route:
                        start_city_old = possible_route[total_dis][0]
                        if start_city_old > start_city:
                            possible_route[total_dis] = (start_city, inter_city, final_city)
                    else:
                        possible_route[total_dis] = (start_city, inter_city, final_city)
        print(self.distance)
        if possible_route == {}:
            return "NONE"
        else:
            max_dis = max(possible_route)
            c1, c2, c3 = possible_route[max_dis]
            return ':'.join([str(max_dis), c1, c2, c3])

# ob=PathCalculator()
# l1='AUS:CHI:200'
# l2='AUS:SEATTLE:100'
# l3='NYC:CLT:100'
# l4='NYC:AUS:4393'
# l5='CHI:AUS:719'
# l6='AUS:LA:2414'
# print(ob.process(l1))
# print(ob.process(l2))
# print(ob.process(l3))
#print(ob.process(l4))
# class PathCalculator:
#     city = dict()
#     def process(self,path):
#         path = path.split(':')
#         if path[0] in self.city:
#             self.city[path[0]][path[1]] = path[2]
#         else:
#             self.city[path[0]] = {path[1]:path[2]}
#
#         if path[1] in self.city:
#             self.city[path[1]][path[0]] = path[2]
#         else:
#             self.city[path[1]] = {path[0]:path[2]}
#
#         if path[0]
#

# ob=PathCalculator()
# l1='AUS:CHI:200'
# l2='AUS:SEATTLE:100'
# l3='NYC:CLT:100'
# l4='NYC:AUS:4393'
# ob.process(l1)
# ob.process(l2)
# # ob.process(l3)
# # ob.process(l4)
# print(ob.city)




# public static int balancedSum(List<Integer> sales) {
#     // Write your code here
# 		int sum =0;
#         for(int i=0;i<list.size();i++){
#             sum += list.get(i);
#         }
#         int curr =list.get(0);
#         for(int i=1;i<list.size();i++){
#             if(curr == sum - curr - list.get(i)){
#                 return i;
#             }
#             curr += list.get(i);
#         }
#         return -1;
#     }
# def balancedSum(s):
#     sum = 0
#     for i in s:
#         sum += i
#     x = s[0]
#     for i in range(1,len(s)):
#         if x == (sum - x - s[i]):
#             return i
#         x += s[i]
#     return -1
# print(balancedSum([1,2,3,4,6]))
from collections import Counter as c
# Print subarray between
# current starting
# and ending points

# a = [25,35,872,228,53,278,872]
# for i in range(len(a)):
#     a[i] = "".join(sorted(str(a[i])))
# pair ={}
# count=0
# for i in range(len(a)):
#     if a[i] in pair:
#         pair[a[i]] +=1
#     else:
#         pair[a[i]] =1
# for keys in pair.keys():
#     count+= pair[keys]*(pair[keys]-1) //2
# print(count)


# import collections
# def anagram(a,b):
#     count = 0
#     if len(a) != len(b):
#         return -1
#
#     dic = collections.Counter(a)
#
#     for i in b:
#         if i in dic:
#             if dic[i]:
#                 dic[i] -= 1
#             else:
#                 count += 1
#         else:
#             count += 1
#     return count

# def getMinimumDifference(a,b):
#     res = []
#     for i,j in zip(a,b):
#         res.append(anagram(i,j))
#     return res

# def traverse(a,s,i,j):
#     if a[i][j] != s:
#         return False
#     if i < len(a)-1 and j < len(a[i])-1 and i>-1 and j>-1:
#         traverse(a,s,i+1,j)
#         traverse(a,s,i,j+1)
#         traverse(a,s,i-1,j)
#         traverse(a,s,i,j-1)
# def prime_count():
#     s = "CABa"
#     Hset = {67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113}
#     s = list(s)
#     asc = []
#     for i in s:
#         asc.append(ord(i))
#     print(asc)
#     for i in range(len(asc)):
#         j = 1
#         while True:
#             if asc[i] in Hset:
#                 asc[i] = chr(asc[i])
#                 break
#             if asc[i]-j in Hset:
#                 asc[i] = chr(asc[i]-j)
#                 break
#             elif asc[i]+j in Hset:
#                 asc[i] = chr(asc[i]+j)
#                 break
#             j+=1
#     print(asc)
#
#
# def solve(a, n, m):
#     # s = set()
#     # for i in range(len(a)):
#     #     for j in a[i]:
#     #         if j not in s:
#     #             s.add(j)
#     for i in range(n):
#         for j in range(m):
#             print(traverse(a,a[i][j],i,j))
#     # print(s)
#
#
# c = [
#     ['B','B','B','B','B','B','B'],
#     ['B','G','G','G','G','B','B'],
#     ['B','G','B','B','G','B','B'],
#     ['B','G','B','B','G','B','B'],
#     ['B','G','G','G','G','B','B'],
#     ['B','B','B','B','B','B','B']
# ]
# def color_loop(n,m,mat):
#     for i in range(0,n):
#         for j in range(0,m):
#             c = mat[i][j]
#             for k in range(j+1,m):
#                 if mat[i][k] != c:
#                     break
#             k-=1
#             if k>j:
#                 for l in range(i+1,n):
#                     if mat[l][k] != c:
#                         break
#                 l-=1
#                 if l>i:
#                     p=k
#                     while p >= j:
#                         if mat[l][p] != c:
#                             break
#                         p -= 1
#                     p+=1
#                     if p == j:
#                         q=l
#                         while q >= i:
#                             if mat[q][p] != c:
#                                 break
#                             q-=1
#                         q+=1
#                         if q==i:
#                             return True
#     return False
# print(color_loop(len(c),len(c[0]),c))

# s = "ab12c"
# t = "1zz456"
# def removeOneDigit(s,t):
#     sList = list(s)
#     tList = list(t)
#     count = 0
#     for i in range(len(tList)):
#         tl = tList.copy()
#         if tList[i].isdigit():
#             tl.pop(i)
#             if s < ''.join(tl):
#                 count+=1
#
#     for i in range(len(sList)):
#         sl = sList.copy()
#         if sList[i].isdigit():
#             sl.pop(i)
#             if ''.join(sl) < t:
#                 count+=1
#     return count

s = "123456 ab-cd+ef"
a = s.split(' ')[0]
b = s.split(' ')[1]
result = 0
sign = '+'
word_before_operator = ""
j=0

for i in range(len(b)):
    if b[i] == '+':
        if sign == '+':
            result += int(word_before_operator)
        elif sign == '-':
            result -= int(word_before_operator)
        sign = '+'
        word_before_operator = ""
    elif b[i] == '-':
        if sign == '+':
            result += int(word_before_operator)
        elif sign == '-':
            result -= int(word_before_operator)
        sign = '-'
        word_before_operator = ""
    else:
        word_before_operator += a[j]
        j+=1
if sign == '+':
    result += int(word_before_operator)
elif sign == '-':
    result -= int(word_before_operator)
print(result)