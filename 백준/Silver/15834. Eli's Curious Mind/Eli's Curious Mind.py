dp = [0, 0, 0, 1]
a, b, c = 1, 1, 2
for n in range(4, 77):
    dp.append(b + c)
    a, b, c = b, c, a + b
tc = 1
while N:=int(input()):
    print(f"Case #{tc}: {dp[N]}")
    tc += 1