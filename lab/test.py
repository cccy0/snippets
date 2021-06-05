a = []


def b(a):
    a.append(1)


b(a)
print(a)
c = '1'


def d(c):
    e = c + '2'
    return e

print(d(c))