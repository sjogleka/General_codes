def numberOfTokens(expiryLimit, commands):
    # Write your code here
    values = dict()
    time = 0

    for c in commands:
        #  extraction values
        action = c[0]
        token_id = c[1]
        time = c[2]

        #  set token
        if action == 0:
            values[token_id] = expiryLimit + time

        #  reset token
        elif action == 1:
            # check if token exists
            if token_id in values.keys():
                expiry_time = values.get(token_id)
                if expiry_time >= time:
                    values[token_id] = values.get(token_id) + expiryLimit - (expiry_time - time)

    # counting values alive after reading all the values
    count = sum(1 for i in values.values() if i >= time)
    return count


print(numberOfTokens(4,[[0,1,1],[0,2,2],[1,1,5],[1,2,7]]))
print(numberOfTokens(3,[[0,1,1],[1,1,4],[1,2,5]]))