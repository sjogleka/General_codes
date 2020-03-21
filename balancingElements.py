def balancingElements(arr):
    print("-----------------------------")
    print(arr)
    n = len(arr)
    odd = 0
    even =0
    leftOdd= [0]*len(arr)
    leftEven = [0] * len(arr)
    rightOdd = [0]*len(arr)
    rightEven = [0]*len(arr)
    for i in range(n):
        print(i,arr[i])
        leftOdd[i] = odd
        leftEven[i] = even
        if i%2==0:
            even+=arr[i]
        else:
            odd+=arr[i]
        #print("Left Odd", leftOdd, "Left Even", leftEven)
    odd = 0
    even= 0
    for i in range(n-1,-1,-1):
        rightOdd[i] = odd
        rightEven[i] = even

        if i%2==0:
            even+=arr[i]
        else:
            odd+=arr[i]

    count = 0
    print("Left Odd",leftOdd,"Left Even",leftEven)
    print("Right Even", rightEven, "Right Odd", rightOdd)
    for i in range(n):
        if leftOdd[i]+rightEven[i] == leftEven[i]+rightOdd[i]:
            #print("Remove index:- ",i)

            #print("Remove character:- ", arr[i])
            count+=1

    print(count)



if __name__ == '__main__':
    num1 = [5,5,2,5,8]
    num2 = [2,2,2]
    num3 = [2, 1,6,4]
    balancingElements(num1)
    balancingElements(num2)
    balancingElements(num3)

