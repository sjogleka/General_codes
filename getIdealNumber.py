'''
3^x5^y is ideal number
'''
l =1
r  =10
def idealCount(l,r):
    count = 0
    if l ==1:
        l+=1
        count+=1
    for i in range(l,r+1):
        num = i

        while num%3==0:
            num//=3

        while num % 5 == 0:
            num //= 5

        if num ==1:
            count+=1
    return count
print(idealCount(1,10))