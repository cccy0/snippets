# https://blog.csdn.net/weixin_34007291/article/details/88755406
def multipliers():
    return [lambda x: i * x for i in range(4)]


print([m(2) for m in multipliers()])

[6, 6, 6, 6]
