g = lambda: [*map(int, input().split())]

R, G, B = g()

a, b, c = R // 3, G // 3, B // 3
ans = a + b + c

l = [R % 3, G % 3, B % 3]
r = sum(i != 0 for i in l)
print(ans + min(max(l), r))