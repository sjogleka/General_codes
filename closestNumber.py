def closestNumber(arr):
    n = len(arr)
    arr.sort()
    sol = [[arr[0], arr[1]]]
    minn = arr[1] - arr[0]

    for i in range(1, n - 1):
        diff = arr[i + 1] - arr[i]
        if diff < minn:
            minn = diff
            sol = [[arr[i], arr[i + 1]]]
        elif diff == minn:
            sol += [[arr[i], arr[i + 1]]]

    for element in sorted(sol):
        print(element[0]," ",element[1])

if __name__ == '__main__':
    print(closestNumber([6,2,4,10]))
    print(closestNumber([4,2,1,3]))