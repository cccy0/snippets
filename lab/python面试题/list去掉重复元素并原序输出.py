l1 = ['b', 'c', 'd', 'c', 'a', 'a']
l2 = list(set(l1))
l2.sort(key=l1.index)
print(l2)
