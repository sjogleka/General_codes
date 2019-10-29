def mctFromLeafValues(A):
    res, n = 0, len(A)
    stack = [float('inf')]
    for a in A:
        while stack[-1] <= a:
            mid = stack.pop()
            res += mid * min(stack[-1], a)
        stack.append(a)
    while len(stack) > 2:
        res += stack.pop() * stack[-1]
    return res


print(mctFromLeafValues([4,6,2]))
print(mctFromLeafValues([5,3,1]))
print(mctFromLeafValues([2,2,1]))