import  collections
def canMakePaliQueries(s, l,r,k):
    queries=[]
    for i in range(len(l)):
        queries.append([l[i],r[i],k[i]])

    print(queries)
    N = 26
    S = len(s) + 1
    ints = list(map(lambda c: ord(c) - ord('a'), s))

    dp = [0] * S
    for i in range(1, S):
        dp[i] = dp[i-1] ^ (1 << ints[i-1])

    ones = lambda x: bin(x).count('1')
    return str(''.join(map(str,[
        int(ones(dp[r+1] ^ dp[l]) >> 1 <= k)
        for l, r, k in queries
    ])))


def canMakePaliQueries_2(s,queries):
    odds = [[False] * 26]
    for i, c in enumerate(s):
        odds.append(odds[i][:])
        odds[i + 1][ord(c) - ord('a')] ^= True
    return [sum(odds[hi + 1][i] ^ odds[lo][i] for i in range(26)) // 2 <= k for lo, hi, k in queries]


#print(canMakePaliQueries("bcba",1,2,1))
#print(canMakePaliQueries("bcba",[1,2,1],[3,3,1],[2,0,0]))
print(canMakePaliQueries("bcbab",[1,1,2],[4,3,3],[3,3,0]))
#print(canMakePaliQueries_2("bcba",[[1,3,2],[2,3,0],[1,1,0]]))