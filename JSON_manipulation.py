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




