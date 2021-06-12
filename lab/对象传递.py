'''
python中函数传参是引用传递还是值传递

答案是对象传递 对象分可变与不可变对象

https://www.cnblogs.com/loleina/p/5276918.html
'''
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
