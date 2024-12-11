g = lambda: map(int, input().split())

input()
x = 0
for a, b in zip(g(), g()):
    print(x:=min(max(b + 1, x), a - 1), end=' ')