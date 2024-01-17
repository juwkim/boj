N, K = map(int, input().split())
l = 1
ans = 0
p = [1]
for _ in range(len(str(N))):
    p.append(p[-1] * 10 % K)
for i in range(N, 0, -1):
    ans = (ans + i * l) % K
    l = l * p[len(str(i))] % K
print(ans)