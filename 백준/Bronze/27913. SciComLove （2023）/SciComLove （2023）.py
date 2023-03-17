from itertools import cycle

input = __import__('sys').stdin.readline
N, Q = map(int, input().split())
check = bytearray(N + 1)

i = 1
cur = 0
for num in cycle((3, 3, 4)):
    check[i] = 1
    cur += 1
    if i + num > N:
        break
    i += num

for _ in range(Q):
    X = int(input())
    if check[X]:
        check[X] = 0
        cur -= 1
    else:
        check[X] = 1
        cur += 1
    print(cur)