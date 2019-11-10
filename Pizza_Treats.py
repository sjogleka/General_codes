

def pizzaTreats1(ar):
    coupon2 = False
    for i in range(len(ar)):
        if (ar[i] > 0):
            if coupon2 == False:
                coupon2 = False if (ar[i] % 2) == 0 else True
            else:
                coupon2 = True if (ar[i] % 2) == 0 else False
        elif (coupon2 == True and ar[i] == 0):
            coupon2 = False
            print("NO")
            return

    if (len(ar) > 0 and coupon2 == False):
        print("YES")
    else:
        print("NO")


pizzaTreats1([1,0,1])
pizzaTreats1([2,3,3,0])
pizzaTreats1([2,3,1])
pizzaTreats1([1,2,1,2])