import json
import collections
def readJson(file):
    d = collections.defaultdict(list)
    op = []

    with open(file) as json_file:
        data = json.load(json_file)
        for i in range(len(data)):
            available_toppings = data[i]['toppings']
            for j in range(len(available_toppings)):
                if available_toppings[j] not in d:
                    d[available_toppings[j]] = 0
                d[available_toppings[j]]+=1
    '''
    t = sorted(d.items(),reverse=True,key=lambda x:x[1])[:20]
    
    for ele in t:
        op.append(ele[0])
    '''
    d = collections.Counter(d).most_common(20)
    for ele in d:
        op.append(ele[0])
    return op




if __name__ == '__main__':
    print(readJson('pizzas.json'))




