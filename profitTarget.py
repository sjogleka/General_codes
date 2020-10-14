def profitTargets(stockProfit,target):
    stock_map = {}
    result = list()
    visited = set()
    for index,stock in enumerate(stockProfit):
        complement = target-stock
        if complement not in stock_map:
            stock_map[stock] = index
        else:
            if index not in visited and stock_map[complement] not in visited:
                visited.add(stock_map[complement])
                visited.add(index)
                result.append([stock_map[complement],index])
    return len(result)


stockProfit = [5,7,9,13,11,6,6,3,3]
target = 12
print(profitTargets(stockProfit,target))