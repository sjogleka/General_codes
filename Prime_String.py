
def check_prime(a):
    for i in range(2, a):
        if a % i == 0:
            return False
    return True

def find_next_prime(n):
    low = n - 1
    high = n + 1
    while True:
        if check_prime(low):
            return low
        elif check_prime(high):
            return high
        else:
            low -= 1
            high += 1

s = "CABa"
strs = ""
for i in range(len(s)):
    if not check_prime(ord(s[i])):
        a = find_next_prime(ord(s[i]))
        strs = strs + chr(a)
    else:
        strs = strs + s[i]
print(strs)