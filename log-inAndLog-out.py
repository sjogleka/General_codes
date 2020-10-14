'''
def processLogs(logs, maxSpan):
    loggedTime = {}
    for log in logs:
        logData = log.split()
        id = int(logData[0])
        if id in loggedTime.keys():
            loggedTime[id] = int(logData[1]) - loggedTime[id]
        else:
            loggedTime[id] = int(logData[1])

    print(loggedTime)
    res = []
    temp = ""
    for key,value in loggedTime.items():
        if value<=maxSpan:
            res.append(str(key))
'''

def processLogs(logs, maxSpan):
    arr = []
    loggedTime = {}
    for log in logs:
        logData = log.split()
        id = int(logData[0])
        if id in loggedTime.keys():
            loggedTime[id] = int(logData[1]) - loggedTime[id]
            print(loggedTime[id])
            if loggedTime[id] <= maxspan:
                arr.append(id)
                arr.sort()

        else:
            loggedTime[id] = int(logData[1])
    for i in range(len(arr)):
        arr[i] = str(arr[i])

    print(arr)
    return arr






logs = ["30 99 sign-in", "30 105 sign-out", "12 100 sign-in", "20 80 sign-in", "12 120 sign-out", "20 101 sign-out",
        "21 110 sign-in"]
maxspan = 20
processLogs(logs, maxspan)