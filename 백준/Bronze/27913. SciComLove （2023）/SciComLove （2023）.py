N, Q = map(int, input().split())

check = set()
i = 1
while i <= N:
    check.add(i)
    i += 3
    if i <= N:
        check.add(i)
        i += 3
        if i <= N:
            check.add(i)
            i += 4

for _ in range(Q):
    X = int(input())
    if X in check:
        check.remove(X)
    else:
        check.add(X)
    print(len(check))