# Wrong Code

def maximumLearning(iv,articles, p):
    max = 0
    ivperPage = []
    for i in range(len(iv)):
        ivperPage.append(articles[i]/iv[i])

    for i in range(len(iv)):
        for j in range(i+1,len(iv)):
            if ivperPage[i]<ivperPage[j]:
                ivperPage[i],ivperPage[j] = ivperPage[j],ivperPage[i]

                iv[i],iv[j] = iv[j],iv[i]

                articles[i],articles[j] = articles[j],articles[i]

    i= 0
    while i <len(iv) and p>0:
        if (2*articles[i]<=p):
            p-=2*articles[i]
            max+=iv[i]
        i+=1
    print(max)
    return max

def product(arr):
    p = 1
    for i in arr:
        p *= i[0]
    return p

from operator import mul
def subset_product(numbers, iv,target, partial=[],res =[]):
    target -=product(partial)
    if  target>=0:
        print("product(%s)<=%s" % (partial, target))
    if target<0:
        return

    for i in range(len(numbers)):
        #print(partial)
        n = numbers[i]
        remaining = numbers[i:]
        subset_product(remaining, target, partial + [(n,i)])


maximumLearning([2,4,4,5],[2,2,3,4],15)
maximumLearning([1,4,6,3],[1,2,2,3],8)
maximumLearning([3,2,2],[3,2,2],9)

subset_product([1,2,2,3],[1,2,2,3,8)