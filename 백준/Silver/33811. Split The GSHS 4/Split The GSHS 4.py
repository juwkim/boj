N = int(input())
S = input()
ans, cur = 0, 0
for i in range(N - 3):
    p = S[i:i+4]
    if p == "SSHS":
        cur += 1
        ans = max(ans, cur)
    elif S[i:i+4] == "GSHS":
        cur = max(0, cur - 1)
print(ans)