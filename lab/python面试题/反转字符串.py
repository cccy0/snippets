a = 'abcd'
res = ''
for i in reversed(a):
    res += i
print(res)


# 更快
b=a[::-1]
print(b)