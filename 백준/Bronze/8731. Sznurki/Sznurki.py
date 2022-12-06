g = lambda: [*map(int, input().split())]

n, w = g()

cnt = 0
val = 0
for num in g():
    if val + num >= w:
        cnt += 1
        val = 0
    else:
        val += num
print(cnt)