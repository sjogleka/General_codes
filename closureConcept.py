increment_by_i = [lambda x: x + i for i in range(10)]
print(increment_by_i[1](3))
print(increment_by_i[3](3))


def create_increment_func(x):
    return lambda y: y + x


increment_by_i = [create_increment_func(i) for i in range(10)]
print(increment_by_i[1](3))
print(increment_by_i[3](3))


x = 'sumedh',
y = ('sumedh',)
z = ('sumedh')
print(type(x))
print(type(y))
print(type(z))