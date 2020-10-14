'''
def maxProfit(costPerCut, salePrice, lengths):
    maxLength = 0
    for i in range(len(lengths)):
        maxLength = max(lengths[i], maxLength)
    helper(lengths, costPerCut, salePrice, 0, maxLength, {})

def helper(lengths,costPerCut, salePrice, l,r,memo):
    res= 0
    print(l,r)
    if l>=r:
        return res
    if str(l)+"_"+str(r) in memo:
        return memo[l+"_"+r]

    rangeL =l
    rangeR = r
    while l<r:
        m1 = l+(r-1)/2
        m2 = m1+1
        if getCost(lengths,costPerCut,salePrice,m1)>getCost(lengths,costPerCut,salePrice,m2):
            r = m1
        else:
            l = m2

    resR = helper(lengths,costPerCut,salePrice,l+1,rangeR,memo)
    resL = helper(lengths, costPerCut, salePrice, l - 1, rangeR, memo)
    res = max(getCost(lengths,costPerCut,salePrice,l),max(res,max(resR,resL)))
    memo[str(rangeL)+"_"+str(rangeR)] = res
    return res

def getCost(nums,cutCost, price, length):
    res = 0
    cost = 0
    if length==0:
        return float("-inf")
    for i in range(len(nums)):
        numOfCuts = nums[i]/length
        res+=numOfCuts*length*price
        cost+=(numOfCuts-1)*cutCost+(1 if nums[i]%length !=0 else 0)*cutCost

    res -=cost
    return res


print(maxProfit(1,10,[30,59,110]))
'''

def maxProfit(cost_per_cut,price, lengths):
    maxLength = max(lengths)
    maxProfit = 0
    for i in range(1,maxLength):
        sumOfLengths = 0
        sumOfCutCounts = 0
        sumOfCutWastes = 0

        for length in lengths:
            sumOfLengths +=length
            if length%i==0:
                sumOfCutCounts+=(length//i-1)
            else:
                sumOfCutCounts += (length//i)

            sumOfCutWastes += (length%i)
        profit = sumOfLengths*price - sumOfCutCounts*cost_per_cut - sumOfCutWastes*price

        maxProfit = max(profit,maxProfit)

    return maxProfit

print(maxProfit(1,10,[30,59,110]))
print(maxProfit(1,10,[26,103,59]))
print(maxProfit(100,10,[26,103,59]))

