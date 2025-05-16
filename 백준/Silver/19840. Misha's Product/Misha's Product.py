n = int(input())
a = list(map(int, input().split()))
cnt, Sum = [0] * 10, [0] * 10
MOD = 10**9 + 7
for num in a:
    l = len(str(num))
    cnt[l] += 1
    Sum[l] += num
ans = 0
for num in a:
    l = len(str(num))
    for i in range(1, 10):
        ans = (ans + num * cnt[i] * pow(10, i, MOD) + Sum[i]) % MOD
    ans = (ans - (pow(10, l, MOD) + 1) * num) % MOD
print(ans)