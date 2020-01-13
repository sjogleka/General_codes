'''
import collections
def minIncrementForUnique(A):
    count = collections.Counter(A)
    taken = []
    ans = 0
    res = []
    for x in range(100000):
        if count[x] >= 2:
            taken.extend([x] * (count[x] - 1))
            res.append(x)
        elif taken and count[x] == 0:
            res.append(x)
            ans += x - taken.pop()
    print(res)
    print(sum(res))
    return ans


def minIncrementForUnique(A):
    A.sort()
    ret = 0
    cur = -1
    res = []
    for num in A:
        cur = max(cur, num)
        res.append(cur)
        ret += cur - num
    return res





# Driver code
#A = [3, 2, 1, 2, 1, 7]
#A = [1,2,2]
A = [4,2,2,4,5]
print(minIncrementForUnique(A))

'''

MAX = 50


def solve(dp, a, low, high, turn):
    # If only one element left.
    if (low == high):
        return a[low] * turn

        # If already calculated,
    # return the value.
    if (dp[low][high] != 0):
        return dp[low][high]

        # Computing Maximum value when element
    # at index i and index j is to be chosed.
    dp[low][high] = max(a[low] * turn + solve(dp, a,
                                              low + 1, high, turn + 1),
                        a[high] * turn + solve(dp, a,
                                               low, high - 1, turn + 1))
    print(dp)

    return dp[low][high]


# Driver Code
if __name__ == "__main__":
    arr = [1, 3, 1, 5, 2]
    n = len(arr)

    dp = [[0 for x in range(MAX)]
          for y in range(MAX)]

    print(solve(dp, arr, 0, n - 1, 1))