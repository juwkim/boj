t1, t2 = map(int, [input(), input()])
count = 1
while t2 >= 0:
    count += 1
    t1, t2 = t2, t1 - t2
print(count)