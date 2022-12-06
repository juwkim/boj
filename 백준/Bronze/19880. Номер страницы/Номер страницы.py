S = input()
n = len(S) // 2
ans = n - S[1:n].count('0')
if len(S) % 2:
    ans -= (S[n] == '0')
else:
    ans -= (S[n] == '0' or int(S[:n]) > int(S[n:]))
print(ans if int(S[0]) else 0)
