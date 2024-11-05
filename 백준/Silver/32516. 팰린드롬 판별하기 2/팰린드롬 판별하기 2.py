N = int(input())
T = input()
ans = 0
for i in range(N >> 1):
    j = N - 1 - i
    if (T[i], T[j]) == ('?', '?'):
        ans += 26
    elif T[i] == '?' or T[j] == '?':
        ans += 1
    elif T[i] != T[j]:
        ans = 0
        break
print(ans)