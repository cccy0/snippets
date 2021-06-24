class Singleton(object):
    def __new__(cls, *args, **kwargs):
        # cls.instance可能会有属性不存在错误
        if hasattr(cls, 'instance'):
            return cls.instance
        # 不要忘记cls参数
        instance = object.__new__(cls, *args, **kwargs)

        cls.instance = instance
        return instance


s = Singleton()
s1 = Singleton()
print(id(s), id(s1))
print('=' * 100)


class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            return super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance


s = Singleton()
s1 = Singleton()
print(id(s), id(s1))


class Foo(Singleton):
    pass


class Bar(metaclass=Singleton):
    pass


class Bar1(object):
    __metaclass__ = Singleton
