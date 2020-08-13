def equalEdgedStrings(arr):
    res = []
    if not arr:
        return res

    for i in range(len(arr)-1):
        if arr[i][0] == arr[i+1][0] and arr[i][len(arr[i])-1] == arr[i+1][len(arr[i+1])-1]:
            res.append("True")
        else:
            res.append("False")

    return (res)
if __name__ == '__main__':
    arr = ["abcd","abdd","da","dd"]
    arr = ["a","a"]
    equalEdgedStrings(arr)
