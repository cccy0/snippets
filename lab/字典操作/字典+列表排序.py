# 按列表元素的长度排序
a = ['123', '2', '22', '2234']
a.sort(key=lambda x: len(x))
print(a)

# 字典key排序
# 声明字典
key_value = {}

# 初始化
key_value[2] = 56
key_value[1] = 2
key_value[5] = 12
key_value[4] = 24
key_value[6] = 18
key_value[3] = 323

print(sorted(key_value))

d = {
    i: key_value[i] for i in sorted(key_value)
}
print(d)

# 根据value排序
# https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
# key_value.items()不可以索引
# 但可以迭代 key是把迭代的每个结果调用key对应的lambda函数 根据函数返回值排序
# sorted返回的结果就是迭代的结果组成的list
# [(key,value),[key,value]]
# 把item[1]改成item[0]就可以根据key排序了
d1 = {
    k: v for k, v in sorted(key_value.items(), key=lambda item: item[1])
}
print(d1)

# list中的字典排序
alist = [{'name': 'a', 'age': 20}, {'name': 'b', 'age': 30}, {'name': 'c', 'age': 25}]

sorted(alist, key=lambda x: x['age'], reverse=True)

# 获取字典key的最大值最小值
max(key_value.keys())

# 字典的key和items的交集 差集 并集

a = {
    'x': 1,
    'y': 2,
    'z': 3
}

b = {
    'w': 10,
    'x': 11,
    'y': 2
}

# Find keys in common
a.keys() & b.keys()  # { 'x', 'y' }
# Find keys in a that are not in b
a.keys() - b.keys()  # { 'z' }
# Find (key,value) pairs in common
a.items() & b.items()  # { ('y', 2) }

# find keys in both
a.keys() | b.keys()

# find (key,value) pairs in both
a.items() | b.items()
# 可以用来合并有相同的key value的两个字典

# 这些运算符当然对value当然无效

# 构造一个字典 他是另外一个字典的子集

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
p1 = {key: value for key, value in prices.items() if value > 200}
tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
p2 = {key: value for key, value in prices.items() if key in tech_names}

