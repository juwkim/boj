import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: map(int, input().split())
for case in range(int(input())):
    g()
    clients = iter(sorted(g(), reverse=True))
    suppliers = iter(sorted(g()))
    ans, balance, need = 0, 0, -1
    for c in input():
        if c == '+':
            balance += next(clients)
        else:
            if need == -1:
                need = next(suppliers)
            if balance >= need:
                balance -= need
                need = -1
            else:
                ans += 1
    print(ans)