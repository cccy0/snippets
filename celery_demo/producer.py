from tasks import add,app

result = add.delay(0,0)
for i in range(1,3):
    add.delay(i,i)

app.send_task('tasks.add', args=(10, 15),)