g = lambda: [*map(int, input().split())]

n, m = g()
seats = g()

orig = m
cnt = 0
while seats[m-1] != orig:
    cnt += 1
    m = seats[m-1]

if cnt == 0:
    print(0)
else:
    print(cnt + 1)