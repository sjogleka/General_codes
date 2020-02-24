#Link - https://www.geeksforgeeks.org/minimum-number-of-jumps-to-reach-end-of-a-given-array/

def minJumps(arr, n):
    jumps = [0 for i in range(n)]
    for i in range(n - 2, -1, -1):
        if (arr[i] == 0):
            jumps[i] = float('inf')
        elif (arr[i] >= n - i - 1):
            jumps[i] = 1
        else:
            min = float('inf')
            for j in range(i + 1, n):
                if (j <= arr[i] + i):
                    if (min > jumps[j]):
                        min = jumps[j]
            if (min != float('inf')):
                jumps[i] = min + 1
            else:
                jumps[i] = min
    return jumps[0]

if __name__ == '__main__':
    print(minJumps([2,1,4,3,2,5,1,6],8))
    print(minJumps([4,3,2,6,8,3,1,9,6,2],10))