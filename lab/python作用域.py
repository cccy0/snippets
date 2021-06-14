# LEGB
'''
L local
E Enclosing
G global
B built in
在python程序中 访问一个变量的顺序就是LEGB
'''

# 全局变量拥有全局作用域
# 局部变量拥有局部作用域

# 当局部作用域想修改全局作用域的变量的时候，就要用到global

a = '123'


def f1():
    global a
    a = '2'


print(a)


# 想修改嵌套作用域的变量，就要用到nonlocal


def f2():
    c = '1'

    def f3():
        nonlocal c
        c = '222'

    f3()
    print(c)


f2()

d = []


def f4():
    d.append(123)


print(d)

# 易错的例子

name = 'legb'


def ff1():
    print(name)


def ff2():
    name = '123'
    ff1()


print(name)
