g = lambda: [*map(int, input().split())]
while sum(s:= g()):
    n, k = s
    safe, broken = 1, k
    for _ in range(n):
        num, txt = input().split()
        if txt == 'SAFE':
            safe = max(safe, int(num))
        else:
            broken = min(broken, int(num))
    print(safe + 1, broken - 1)