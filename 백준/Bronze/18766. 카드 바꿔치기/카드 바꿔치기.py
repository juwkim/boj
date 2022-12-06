g = lambda: sorted(input().split())
for _ in range(int(input())):
    input()
    print('NOT ' * (g() == g()) + 'CHEATER')