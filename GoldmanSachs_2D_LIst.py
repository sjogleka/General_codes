def sum_2d(arr,k):
    sum = 0
    print("\nFinding Sum of each row:\n")
    dict={}
    for i in range(len(arr)):
        for j in range(len(arr)):
            # Add the element
            sum += arr[i][j]
        dict[i]=sum
        sum = 0
        #print("Sum of the row", i, "=", dict)
    sorted_dict = sorted(dict.items(), key=lambda kv: kv[1],reverse=True)
    #print("Sum of the row", i, "=", sorted_dict)
    print(arr[sorted_dict[k - 1][0]])
    return sorted_dict[k - 1][0]

if __name__ == '__main__':
    a = [[80, 96, 81,77], [78, 71, 93,75],[71,98,70,95],[80,96,89,77]]
    b = [[74,92,75,73],[74,92,75,73],[73,88,99,80]]
    c =[[74,92,75,73],[74,92,75,73],[74,92,75,73]]
    k = 3
    ans = sum_2d(c,k)
    print(ans)
    # print(dict[k-1][0])