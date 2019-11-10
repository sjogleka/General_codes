class PathCalculator:
    distance = {}  # dictionary that maintains distance between cities
    def process(self, line: str) -> str:
        if line == None:
            return "NONE"
        possible_route = {}
        city1, city2, dis = list(line.split(':'))
        if not city1 in self.distance:
            self.distance[city1] = {}
        self.distance[city1][city2] = int(dis)
        if not city2 in self.distance:
            self.distance[city2] = {}
        self.distance[city2][city1] = int(dis)
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

        if possible_route == {}:
            return "NONE"
        else:
            max_dis = max(possible_route)
            c1, c2, c3 = possible_route[max_dis]
            return ':'.join([str(max_dis), c1, c2, c3])

ob=PathCalculator()
l1='SEA:NYC:200'
l2='CHI:AUS:200'
l3='NYC:AUS:1000'
l4='NYC:HAWAII:4393'
l5='CHI:AUS:719'
l6='AUS:LA:2414'
print(ob.process(l1))
# print(ob.process(l2))
# print(ob.process(l3))
# # print(ob.process(l4))
# # print(ob.process(l5))
# # print(ob.process(l6))

ob=PathCalculator()
l1='CHI:NYC:200'
l2='SEATTLE:LA:200'
l3='NYC:SEATTLE:1000'
ob.process(l1)
ob.process(l2)
ob.process(l3)