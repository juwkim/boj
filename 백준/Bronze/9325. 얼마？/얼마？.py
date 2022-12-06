T = int(input())
for _ in range(T):
    s, n = int(input()), int(input())
    options = [list(map(int, input().split())) for _ in range(n)]
    s += sum([option[0] * option[1] for option in options])
    print(s)