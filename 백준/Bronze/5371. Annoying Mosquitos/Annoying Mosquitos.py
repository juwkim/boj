import sys
input = sys.stdin.readline

g = lambda: tuple(map(int, input().split()))

for _ in range(int(input())):
    cnt = 0
    pos = {g() for _ in range(int(input()))}
    for _ in range(int(input())):
        x, y = g()
        tmp = {i for i in pos if (abs(i[0] - x) <= 50) * (abs(i[1] - y) <= 50)}
        cnt += len(tmp)
        pos -= tmp
    print(cnt)