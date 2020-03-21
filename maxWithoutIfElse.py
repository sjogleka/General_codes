def maxWithoutif(a,b):
    return (a>b)*a + (b>a)*b

def minWithoutif(a,b):
    return (a>b)*b + (b>a)*a

print(maxWithoutif(6,5))
print(minWithoutif(6,5))
