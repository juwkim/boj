g = lambda: [*map(int, input().split())]

N, *l = g()
a, b = sorted(l)
ans = 1
while True:
    if b - a == 1 and a&1:
        break
    
    a = (a + 1) // 2
    b = (b + 1) // 2
    ans += 1

print(ans)