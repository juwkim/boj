g = lambda: map(int, input().split())
input()
ans, t, a = -1, -1, 0
for T, A in zip(g(), g()):
    ans = max(ans, (t:=t+T) // (a:=a+A))
print(ans * 5 + 5)