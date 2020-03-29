def restock(itemCount,target):
    keepingAdding=0

    for i in range(len(itemCount)):
        keepingAdding+=itemCount[i]
        if keepingAdding>=target:
            break

    if keepingAdding>=target:
        return keepingAdding-target
    else:
        return target-keepingAdding


if __name__ == '__main__':
    print(restock([10,20,30,40,15],80))
    print(restock([6,1,2,1], 100))
    print(restock([1,2,3,2,1], 4))