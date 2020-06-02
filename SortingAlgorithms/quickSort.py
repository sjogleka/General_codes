import random

def qucikSort(arr):
    return inplaceQuickSort(arr,0,len(arr)-1)


def inplaceQuickSort(array,start,stop):
    if start<stop:
        left = start
        right = stop
        pivot = random.randint(left,right)
        print(pivot)
        while left<=right:
            while array[left]< array[pivot]:
                left+=1
            while array[right]>array[pivot]:
                right-=1

            if left<=right:
                array[left],array[right] = array[right],array[left]
                left+=1
                right-=1

            inplaceQuickSort(array,start,right)
            inplaceQuickSort(array, left, stop)

    return array

if __name__ == '__main__':
    x = [4,5,1,11,13,60]
    print(qucikSort(x))