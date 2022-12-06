N, M = input().split()
R, cc = map(int, M.split(','))
ans, Max = -1, -1
for _ in range(int(N)):
    name, M = input().split()
    a, b = map(int, M.split(','))
    cost = a * 100 + b
    if Max < cost and a <= R and b <= cc:
        ans = name
        Max = cost
print(ans)