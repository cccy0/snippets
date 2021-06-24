list1 = [1, 2, 3]
list2 = [3, 4, 5]

# 相同元素
res = []
for i in list1:
    if i in list2:
        res.append(i)
print(res)

# 不同元素 把两个列表中的相同元素剔除掉
res1 = []
for i in list1:
    if i not in res:
        res1.append(i)

for i in list2:
    if i not in res:
        res1.append(i)

print(res1)

#集合
set1=set(list1)
set2=set(list2)
same_list=list(set1 & set2)
diff_list=list(set1 ^ set2)
print(same_list,diff_list)
