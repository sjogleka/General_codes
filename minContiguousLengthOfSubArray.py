'''
def twoIntegers(A,s):
    op = []
    for i in range(len(A)):
        sum =A[i]
        for j in range(i+1,len(A)):
            #print("i",A[i],"j",A[j])
            sum+=A[j]
            if sum>=s:
                if len(op)==0 or j-i<len(op):
                    op =A[i:j+1]
                    break
    print(op)
    return len(op)
'''
import math
def twoIntegers(A,s):
    window_sum,window_start = 0,0
    min_length = math.inf
    for end in range(len(A)):
        window_sum+=A[end]
        while window_sum>=s:
            prev = min_length
            min_length = min(min_length,end-window_start+1)
            if min_length<prev:
                op = A[window_start:end + 1]
            window_sum-=A[window_start]
            window_start+=1

    print(op)
    return min_length



if __name__ == '__main__':
    s = 7
    #s = 6
    #s =20
    #s = 1
    A = [2,3,1,2,4,3]
    #A = [1,1,2,2,2,1,1]
    #A = [2,3,1,2,4,3]
    #A = []
    #Output =2

    print(twoIntegers(A,s))
