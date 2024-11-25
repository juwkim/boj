N, M, *nums = map(int, open(0).read().split())
S = {*nums}
Min = 1
while Min in S: Min += 1
Max = (N + Min**2 - 1) // Min**2
while Max in S: Max += 1
P = sorted({*range(Min, Max + 1)} - S)
ans = 1e9
for x in P:
    for y in P:
        mul = x * y
        for z in P:
            num = mul * z
            ans = min(ans, abs(N - num))
            if num >= N:
                break
print(ans)