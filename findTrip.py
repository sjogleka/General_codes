'''
GIVEN A LIST OF FLIGHTS (IN ANY ORDER), CONSTRUCT THE TRIP
THAT THIS LIST REPRESENTS. FOR EXAMPLE, IF WE HAVE A FLIGHT
FROM SAN FRANCISCO TO DALLAS AND A FLIGHT FROM LOS ANGELES
TO SAN FRANCISCO, THE TRIP IS "LAX TO SFO TO DFW".

ASSUMPTIONS:
EACH CITY WILL BE VISITED ONLY ONCE.
THE LIST WILL ONLY REPRESENT ONE SINGLE TRIP.

FLIGHTS = [('SFO', 'DFW'), ('LAX', 'SFO'), ('DFW', 'CLT')]
TRIP: ['LAX', 'SFO', 'DFW', 'CLT']

IF THE ABOVE WORKS, TRY YOUR PROGRAM WITH THE FOLLOWING INPUT:
FLIGHTS = [('DFW','CLT'), ('SFO','DFW'), ('WAS','NYK'), ('LAX','SFO'), ('CLT','WAS')]
TRIP: ['LAX', 'SFO', 'DFW', 'CLT', 'WAS', 'NYK']
'''

#flight = [('SFO','DFW'),('LAX','SFO'),('DFW','CLT')]
#flight = {'SFO':'DFW','LAX':'SFO','DFW':'CLT'}
flight = {'DWF':'CLT','SFO':'DWF','WAS':'NYK','LAX':'SFO','CLT':'WAS'}
tmp = []
op  =[]
for k,v in flight.items():
    res = []
    tmp.append(v)
    res.append(k)
    res.append(v)
    while tmp:
        data = tmp.pop(0)
        if data in flight.keys():
            tmp.append(flight[data])
            res.append(flight[data])
    if len(res)>len(op):
        op = res

print(op)






