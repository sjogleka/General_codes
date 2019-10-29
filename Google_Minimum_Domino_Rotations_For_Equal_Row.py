# Leetcode - 1007 - https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/
# Google - https://leetcode.com/discuss/interview-question/352460/Google-Online-Assessment-Questions

import  collections
def minDominoRotations(A, B):
    """
    :type A: List[int]
    :type B: List[int]
    :rtype: int
    """
    n = len(A)
    d = collections.defaultdict(int)
    maxVal = float('-inf')
    num = 0  # num: highest frequency occurred
    # only count the num occurred most frequently
    for i in range(n):
        d[A[i]] += 1
        d[B[i]] += 1
        if d[A[i]] > maxVal:
            maxVal = d[A[i]]
            num = A[i]
        if d[B[i]] > maxVal:
            maxVal = d[B[i]]
            num = B[i]
    # if the frequency of the num < n, there's no reason it can be achieved the same number in whole row
    if maxVal < n:
        return -1

    cntRotate = 0  # count one of the sides to achieve all numbers are same in B
    skipRotate = 0  # when two sides are same as the num occurred most frequently
    for i in range(n):
        if A[i] != num and B[i] != num:  # non of sides are same as the num
            return -1
        if A[i] == num and B[i] == num:  # two sides are same as the num, so do not need to rotate
            skipRotate += 1
            continue
        if A[i] == num:  # if A's side is same as the num, rotate it the B side
            cntRotate += 1
    # count the minimum rotation:
    # min(all the numbers in B are same after rotation, all the numbers in A are same after rotation)
    return min(cntRotate, n - skipRotate - cntRotate)


print(minDominoRotations([1,2,3,6,3,2],[2,1,2,2,2,4]))
print(minDominoRotations([1,2,1,2],[2,6,1,2]))