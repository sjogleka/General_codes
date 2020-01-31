def countBits(a, b):
    count = 0
    while (a or b):
        last_bit_a = a & 1
        last_bit_b = b & 1
        if (last_bit_a != last_bit_b):
            count += 1
        a = a >> 1
        b = b >> 1
    return count
a = 6
b = 9
print(countBits(a, b))

################################

def countSetBits( n ):
	count = 0
	while n:
		count += n & 1
		n >>= 1
	return count

def FlippedCount(a , b):
	return countSetBits(a^b)

a1 = 6
b1 = 9
print(FlippedCount(a1, b1))


def ChangeBits(x,y):
    result = -404
    count = 0
    while(x or y):
        last_bit_x = x&1
        last_bit_y = y&1
        if last_bit_x != last_bit_y:
            count+=1
        x =x>>1
        y = y>>1
    result = count
    print(result)

ChangeBits(a,b)
