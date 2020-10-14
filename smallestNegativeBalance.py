def smallest_negative_balance(balances):
    people = set()
    for record in balances:
        people.add(record[0])
        people.add(record[1])

    balance = {person: 0 for person in people}
    for record in balances:
        balance[record[0]] -= record[2]
        balance[record[1]] += record[2]
    ret = []
    smallest_balance = float('inf')
    for person, bal in balance.items():
        smallest_balance = min(smallest_balance, bal)

    if smallest_balance >= 0:
        return ["Nobody has a negative balance"]

    for person, bal in balance.items():
        if bal == smallest_balance:
            ret.append(person)
    ret.sort()
    return ret


print(smallest_negative_balance([['Alex', 'Blake', 2], ['Blake', 'Alex', 2],['Casey', 'Alex', 5], ['Blake', 'Casey', 7], ['Alex', 'Blake', 4],['Alex', 'Casey', 4]]))
print(smallest_negative_balance([['Alex', 'Blake', 5], ['Blake', 'Alex', 3],['Casey', 'Alex', 7], ['Blake', 'Casey', 4], ['Alex', 'Blake', 2]]))
print(smallest_negative_balance([['Blake', 'Alex', 7],['Blake', 'Alex', 3],['Alex', 'Blake', 4],['Blake', 'Alex', 1],['Alex', 'Blake', 7]]))