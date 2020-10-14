def permute(nums):
    def backtrack(first=0):
        if first == n:
            if int(''.join(map(str, nums)))%8==0:
                print("Found")
                return True
        for i in range(first, n):
            nums[first], nums[i] = nums[i], nums[first]
            op1 = backtrack(first + 1)
            if op1:
                return  True
            nums[i], nums[first] = nums[first], nums[i]

        return False

    n = len(nums)
    temp = backtrack()
    if temp == True:
        return "YES"
    else:
        return "NO"

def checkDivisibility_1(arr):
    op = []
    for i in range(len(arr)):
        arr[i]  = list(map(int, str(arr[i])))
        op.append(permute(arr[i]))

    return op


def checkDivisibility(arr):
    result = [''] * len(arr)
    for i in range(len(arr)):
        result[i] = solve(arr[i])

    return result

def solve(num):
    number = str(num)
    l = len(number)
    if l == 1:
        if int(number) % 8 == 0:
            return "YES"
        else:
            return "NO"
    elif l == 2:
        if int(number) % 8 == 0 or int(number[::-1]) % 8 == 0:
            return "YES"
        else:
            return "NO"

    # when there are 3 or more digits
    hm = [0 for _ in range(10)]
    for char in number:
        hm[int(char)] += 1

    for i in range(0, 1000, 8):
        copy = list(hm)
        s = "00" + str(i)
        j = -1
        while j >= -3:  # check 3 digits
            d = int(s[j])
            if copy[d] <= 0: break
            copy[d] -= 1
            j -= 1
        if j == -4:
            return "YES"
    return "NO"




if __name__ == '__main__':
    print(checkDivisibility_1([61,75,0]))
    #print(solve(75))
    #print(solve(2729898085))
    #arr = [123, 1312, 777777, 7001]
    arr = [41,2729898085]
    #arr = [8,86,656411992834780769]
    print(checkDivisibility(arr))

    #print(result)

    print()