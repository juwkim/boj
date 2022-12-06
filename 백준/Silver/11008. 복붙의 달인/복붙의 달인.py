S = lambda: input().split()
I = lambda: int(input())

for _ in range(I()):
    s, p = S()
    ans = len(s) + (1 - len(p)) * s.count(p)
    print(ans)