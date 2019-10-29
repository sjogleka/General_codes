def binarySearch(arr, low, high, x):
    if (high >= low):

        mid = low + (high - low) // 2
        if x == arr[mid]:
            return (mid)
        elif (x > arr[mid]):
            return binarySearch(arr, (mid + 1), high, x)
        else:
            return binarySearch(arr, low, (mid - 1), x)

    return -1


# Returns count of pairs with
# difference k in arr[] of size n.
def countPairsWithDiffK(arr, n, k):
    count = 0
    arr.sort()  # Sort array elements
    s = set()
    for i in range(0, n - 2):
        mid = binarySearch(arr, i + 1, n - 1,abs(arr[i] - k))
        if (mid != -1):
            count += 1
            s.add((arr[i],arr[mid]))

    print(s)
    return len(s)


# Driver Code
# arr = [1, 5, 3, 4, 2]
# arr = [6,6,3,9,3,5,1]
arr = [1,3,46,1,3,9]
n = len(arr)
k = 47
print("Count of distinct pairs with given sum is ",
      countPairsWithDiffK(arr, n, k))