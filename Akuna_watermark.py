from datetime import datetime
class HashTable:
    def __init__(self, rawEvents):
        self.hwm = None
        self.hashtable = {}
        for i in rawEvents:
            query = i.split('|')
            self.operate_HT(query)

    def operate_HT(self,query):
        if query[1] == 'INSERT':
            self.insert(query[2],query[3])
        elif query[1] == 'UPSERT':
            self.upsert(query[2], query[3])
        elif query[1] == 'DELETE':
            self.delete(query[2])
        x = int(query[0])/1000
        self.hwm = datetime.utcfromtimestamp(x)

    def insert(self,key,value):
        if key not in self.hashtable:
            self.hashtable[key] = value
    def upsert(self,key, value):
        self.hashtable[key] = value

    def delete(self,key):
        if key in self.hashtable:
            self.hashtable.pop(key)
    def table(self):
        print(self.hashtable)
        return self.hashtable

    def high_watermark(self):
        return self.hwm

h = HashTable(['1563454984001|INSERT|test|123','1563454984002|UPSERT|test|123','1563454984003|DELETE|test'])

s = h.table