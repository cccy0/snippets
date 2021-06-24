# 创建一个生成器
def get_lines():
    with open('file.txt', 'r') as f:
        for i in f:
            yield i


# 上一种方法读取次数太多

bufsize = 2
with open('file.txt') as infile:
    while True:
        lines = infile.readlines(bufsize)
        if not lines:
            break
        for line in lines:
            print(line)


for i in get_lines():
    print(i)

# https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do
# mmap