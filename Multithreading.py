import  threading

''' 
IMP to note: - Here we might get output 98 or 99 as we are using  += operation which is not atomic and hence GIL
might drop lock in between and n will get updated to another value. Another thing to note that most of the operations 
are atomic in python and hence we dont need to make then thread safe. e.g list.sort() are thread safe and hence 
this operation will either happen or wont there is no intermediate stage.

Follow a simple rule: Always lock around reads and writes of shared mutable state.

'''


threads = []
n = 0
lock = threading.Lock()

def foo():
    global n
    n +=1


def foo1():
    global n
    with lock: # this will make += thread safe
        n +=1

for i in range(100):
    t = threading.Thread(target=foo)
    threads.append(t)

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print(n)