
'''
def solutions(S, C):
    minCost = 0

    for i in range(len(S) - 1):
        if S[i] == S[i + 1]:
            minCost += getMin(i, C)

    return minCost


def getMin(n, C):
    if C[n] < C[n + 1]:
        return C[n]
    else:
        return C[n + 1]

'''
def solution(S,C):
    total = 0
    i,j = 0,0
    while i<len(S):
        maxConsec = -float('inf')
        subtotal = 0
        while j<len(S) and S[j]==S[i]:
            subtotal+=C[j]
            maxConsec =  max(maxConsec,C[j])
            j+=1
        #print("subtotal",subtotal,"max",maxConsec)
        total+=(subtotal-maxConsec)
        i= j
    print(total)



if __name__ == '__main__':
    solution("abccbd",[0,1,2,3,4,5])
    solution("aaa", [4,3,5])