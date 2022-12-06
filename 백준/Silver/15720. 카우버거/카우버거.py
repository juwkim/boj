g = lambda: [*map(int, input().split())]

B, C, D = g()
a = sorted(g(), reverse=True)
b = sorted(g(), reverse=True)
c = sorted(g(), reverse=True)
ans = sum(sum(i) for i in [a, b, c])
print(ans)

ans = sum(x + y + z for x,y,z in zip(a, b, c)) * 9 // 10
idx = min(B, C, D)
ans += sum(a[idx:]) + sum(b[idx:]) + sum(c[idx:])
print(ans)