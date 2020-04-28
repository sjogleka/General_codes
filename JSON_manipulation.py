import json
import requests
'''
searchFor = input("Search For")
temp = requests.get("https://jsonmock.hackerrank.com/api/movies/search/?Title="+searchFor)
data = temp.json()
total_pages = data['total_pages']
res =[]
for i in range(total_pages):
    data2  = requests.get("https://jsonmock.hackerrank.com/api/movies/search/?Title=" + searchFor+"&page="+str(i)).json()['data']
    for ele in range(len(data2)):
        print(data2[i])
        res.append(data2[i]['Title'])
print(res)
print(sorted(res))
'''

data = json.load(open('read_json.json','r'))

print(data)
source = data['origin_addresses'][0]
destinations = data['destination_addresses']
entries = data['rows'][0]['elements']


#print(source)
#print(destinations,len(destinations))
#print(entries,len(entries))


res= []
for i in range(len(destinations)):
    res.append((destinations[i],entries[i]['distance']['text'],entries[i]['duration']['text']))
print("Source\t\t\t\t Destination\t\t\t\t Distance\t\t\t\t Duration")
for i in range(len(res)):
    temp  = res[i][0].split(',')
    temp = ','.join(temp[:-1])
    #print(temp)
    print(','.join(source.split(',')[:-1]),"\t",temp,"\t\t",res[i][1],"\t\t",res[i][2])

