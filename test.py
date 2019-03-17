from tasks import add

for i in range(100):
    add.delay(i, i)

