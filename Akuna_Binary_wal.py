import codecs
import re
from datetime import datetime
'''
class WAL(object):
    def __init__(self,binary_wal):
        self.binary_wal = binary_wal.hex()
        self.res = []


    def get_events(self):
        a = []
        a.append(str(int(self.binary_wal[:16], 16)))
        if int(self.binary_wal[16:18], 16) == 0:
            a.append("INSERT")
        elif int(self.binary_wal[16:18], 16) == 1:
            a.append("UPSERT")
        if int(self.binary_wal[16:18], 16) == 2:
            a.append("DELETE")
        key_length = int(self.binary_wal[18:22], 16)
        key_length = (key_length * 2)
        key_value = codecs.decode(self.binary_wal[22:22 + key_length], "hex")
        key_value = str(key_value)
        key_value = key_value.replace("b'", '')
        key_value = key_value.replace("'", "")
        a.append(key_value)
        if int(self.binary_wal[16:18],16)!=2:
            value_length = int(self.binary_wal[22 + key_length:22+ key_length+4],16)
            value_length = 22 + key_length + 4
            value_value = str(codecs.decode(self.binary_wal[value_length:], "hex"))
            value_value = value_value.replace("b'", '')
            value_value = value_value.replace("'", "")
            a.append(value_value)

        x = '|'.join(a)
        self.res.append(x)
        return sorted(self.res,key=lambda a :a[0])
'''

def bytes_to_int(bytes):
    result = 0
    for b in bytes:
        result = result * 256 + int(b)
    return result

def wal(a):
    n = 0
    while n < len(a):
        if len(a)==0:
            print("..........")
        epoch = bytes_to_int(a[:8])
        #print(a[:8])
        res.append(str(epoch))
        #########################################
        msg_id = bytes_to_int(a[8:9])
        if msg_id == 0:
            res.append("INSERT")
        elif msg_id == 1:
            res.append("UPSERT")
        elif msg_id == 2:
            res.append("DELETE")
        # res.append(str(msg_id))
        #########################################
        key_length = bytes_to_int(a[9:11])
        # res.append(key_length)
        key_value = a[11:11 + key_length].decode('utf-8')
        buf = 11 + key_length
        res.append(key_value)
        #########################################
        if msg_id != 2:
            value_length = bytes_to_int(a[buf:buf+2])
            if value_length<=0:
                return res
            # res.append(value_length)
            buf2 = buf + 2
            value_string = a[buf2:buf2+value_length].decode('utf-8')
            res.append(value_string)
        #########################################
        #print(res)
        else:
            buf2 = buf
            value_length = 0
        x = '|'.join(res)
        print(x)
        n +=len(a[:buf2+value_length])
        #print(n)
        if n!=len(a):
            a =a[n:]

if __name__ == '__main__':

    #print(WAL(b'\x00\x00\x01l\x05-\xcfA\x00\x00\x0etest_key_09812\x00\x10test_value_12876').get_events())
    #temp = '0000016c052dcf4100000e746573745f6b65795f30393831320010746573745f76616c75655f3132383736'
    temp1 = '0000016c052dcf4101000d746573745f6b65795f313233340012746573745f76616c75655f31323339393038'
    temp2 = '0000016c052dcf4102000f746573745f6b65795f313233383937'
    #print(bytes.fromhex('0000016c052dcf42'))
    temp = bytes.fromhex('0000016c052dcf4100000e')
    x = '0000016c052dcf4100000e746573745f6b65795f30393831320010746573745f76616c75655f31323837360000016c052dcf4101000d746573745f6b65795f313233340012746573745f76616c75655f31323339393038'
    all = bytes.fromhex(x)
    upsert = bytes.fromhex(temp1)
    delete = bytes.fromhex(temp2)
    #insert = b'\x00\x00\x01l\x05-\xcfB\x00\x00\x0etest_key_09812\x00\x10test_value_12876'
    insert = b''
    new = [all]
    res = []
    #st = '\x00\x00\x01l\x05-\xcfA\x00\x00\x0etest_key_09812\x00\x10test_value 12876'
    for i in range(len(new)):
        wal(new[i])



