from tasks import add

result = add.delay(0,0)
for i in range(1,3):
    add.delay(i,i)
