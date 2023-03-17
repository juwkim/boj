from itertools import cycle

N, Q = map(int, input().split())
check = set()
i = 1

for num in cycle((3, 3, 4)):
    check.add(i)
    if i + num > N:
        break
    i += num

cur = len(check)
for _ in range(Q):
    X = int(input())
    if X in check:
        check.remove(X)
        cur -= 1
    else:
        check.add(X)
        cur += 1
    print(cur)