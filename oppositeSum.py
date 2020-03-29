def reverse(Number):
    Reverse = 0
    while (Number > 0):
        Reminder = Number % 10
        Reverse = (Reverse * 10) + Reminder
        Number = Number // 10
    return (Reverse)


def oppositesum(arr):
    output = 0
    pairs = set()
    rev = {}
    #     arr = list(set(arr))
    for i in range(len(arr)):

         += 1
        if arr[i] not in rev.keys():
            rev[arr[i]] = reverse(arr[i])
        for j in range(i + 1, len(arr)):
            if arr[j] not in rev.keys():
                rev[arr[j]] = reverse(arr[j])
            if (arr[i], arr[j]) in pairs:
                output += 1
            elif (arr[i] + rev[arr[j]]) == (rev[arr[i]] + arr[j]):
                pairs.add((arr[i], arr[j]))
                output += 1
    return output

if __name__ == '__main__':
    print(oppositesum([1,20,2,11]))