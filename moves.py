def moves(arr):
    count,low,high  = 0,0,len(arr)-1
    while low < high:
        while arr[low]%2==0 and low<high:
            low+=1
        while arr[high]%2==1 and low<high:
            high-=1
        if low<high:
            arr[low],arr[high] = arr[high],arr[low]
            low+=1
            high-=1
            count+=1
    return count


if __name__ == '__main__':
    print(moves([8,5,11,4,6]))