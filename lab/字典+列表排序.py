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

d={
    i:key_value[i] for i in sorted(key_value)
}
print(d)

# 根据value排序
# https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
d1={
    k:v for k,v in sorted(key_value.items(),key=lambda item:item[1])
}
print(d1)


# list中的字典排序
alist = [{'name':'a','age':20},{'name':'b','age':30},{'name':'c','age':25}]

sorted(alist,key=lambda x:x['age'],reverse=True)