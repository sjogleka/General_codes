def func1(x, y, count, a):
    if count == len(a):
        return var
    #var = f"rod_{count}"
    for i in range(0, len(x)):
        for j in range(0, len(y)):
            if count == 2:
                if i != j:
                    var.append([x[i], y[j]])
                    print([x[i], y[j]])
            else:

                if y[j] not in x[i]:
                    var.extend(x[i])
                    var.extend(y[j])
                    #print([x[i],y[j]])

    count = count + 1
    x = var
    return func1(x, y, count, a)
var = []
print(func1(list('12345'), list('12345'), 2, '12345'))