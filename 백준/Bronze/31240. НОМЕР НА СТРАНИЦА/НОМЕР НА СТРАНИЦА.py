l = len(S := input())
ans = 0
for i in range(l - 1 >> 1):
    if S[0] == '0' or S[i + 1] == '0':
        continue
    ans += 1
if l % 2 == 0 and S[0] != '0' and S[l >> 1] != '0':
    ans += S[:l >> 1] <= S[l >> 1:]
print(ans)