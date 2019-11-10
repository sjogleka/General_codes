def getUnallottedUsers(bids, totalShares):
    price_dict = dict()
    output = []
    for i in bids:
        if i[2] not in price_dict:
            price_dict[i[2]] = [[i[0], i[1], i[3]]]
        else:
            price_dict[i[2]].append([i[0], i[1], i[3]])
    for i in price_dict:
        price_dict[i] = sorted(price_dict[i], key=op.itemgetter(2))
    while totalShares > 0:
        max_price = max(price_dict.keys())
        if len(price_dict[max_price]) == 1:
            print(price_dict)
            print(price_dict[max_price])
            totalShares -= price_dict[max_price][0][1]
            price_dict.pop(max_price)
        else:
            if (totalShares // len(price_dict[max_price])) > 0:
                x = totalShares // len(price_dict[max_price])
                for i in price_dict[max_price]:
                    i[1] -= x
                    totalShares -= x
                y = totalShares % len(price_dict[max_price])
                i = 0
                while y > 0 and i < len(price_dict[max_price]):
                    if price_dict[max_price][i][1] == 0:
                        i += 1
                        continue
                    price_dict[max_price][i][1] -= 1
                    totalShares -= 1
                    i += 1
                    y -= 1
            else:
                y = totalShares % len(price_dict[max_price])
                i = 0
                while y > 0 and i < len(price_dict[max_price]):
                    price_dict[max_price][i][1] -= 1
                    totalShares -= 1
                    i += 1
                    y -= 1
                for j in range(i, len(price_dict[max_price]) - 1):
                    output.append(price_dict[max_price][i][0])

            price_dict.pop(max_price)

    for key in price_dict:
        for i in range(0, len(price_dict[key])):
            output.append(price_dict[key][i][0])

    return output